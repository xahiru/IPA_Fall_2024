interface User {
  name: string;
  email: string;
  password: string;
}

interface AuthResponse {
  user: Omit<User, 'password'>;
  token: string;
}

class AuthError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'AuthError';
  }
}

// Helper functions
const generateToken = (): string => {
  return Math.random().toString(36).substring(2) + Date.now().toString(36);
};

const validateEmail = (email: string): boolean => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

const validatePassword = (password: string): boolean => {
  return password.length >= 6;
};

const getUsers = (): User[] => {
  try {
    return JSON.parse(localStorage.getItem('users') || '[]');
  } catch {
    return [];
  }
};

const saveUsers = (users: User[]): void => {
  localStorage.setItem('users', JSON.stringify(users));
};

export const registerUser = async (user: User): Promise<AuthResponse> => {
  // Validate input
  if (!user.email || !user.password || !user.name) {
    throw new AuthError('All fields are required');
  }

  if (!validateEmail(user.email)) {
    throw new AuthError('Invalid email format');
  }

  if (!validatePassword(user.password)) {
    throw new AuthError('Password must be at least 6 characters long');
  }

  // Simulate network delay
  await new Promise(resolve => setTimeout(resolve, 300));

  const users = getUsers();

  // Check if user already exists
  if (users.some(u => u.email.toLowerCase() === user.email.toLowerCase())) {
    throw new AuthError('User already exists');
  }

  // Add new user
  const newUser = {
    ...user,
    email: user.email.toLowerCase(),
  };

  users.push(newUser);
  saveUsers(users);

  // Return user data without password and generate token
  const { password, ...userWithoutPassword } = newUser;
  const token = generateToken();

  // Store current session
  sessionStorage.setItem('currentUser', JSON.stringify(userWithoutPassword));
  sessionStorage.setItem('token', token);

  return {
    user: userWithoutPassword,
    token,
  };
};

export const loginUser = async (email: string, password: string): Promise<AuthResponse> => {
  // Validate input
  if (!email || !password) {
    throw new AuthError('Email and password are required');
  }

  if (!validateEmail(email)) {
    throw new AuthError('Invalid email format');
  }

  // Simulate network delay
  await new Promise(resolve => setTimeout(resolve, 300));

  const users = getUsers();
  const user = users.find(
    u => u.email.toLowerCase() === email.toLowerCase() && u.password === password
  );

  if (!user) {
    throw new AuthError('Invalid email or password');
  }

  // Generate token and prepare response
  const { password: _, ...userWithoutPassword } = user;
  const token = generateToken();

  // Store current session
  sessionStorage.setItem('currentUser', JSON.stringify(userWithoutPassword));
  sessionStorage.setItem('token', token);

  return {
    user: userWithoutPassword,
    token,
  };
};

export const updateUserPassword = async (email: string, newPassword: string): Promise<void> => {
  // Validate input
  if (!email || !newPassword) {
    throw new AuthError('Email and new password are required');
  }

  if (!validateEmail(email)) {
    throw new AuthError('Invalid email format');
  }

  if (!validatePassword(newPassword)) {
    throw new AuthError('New password must be at least 6 characters long');
  }

  // Simulate network delay
  await new Promise(resolve => setTimeout(resolve, 300));

  const users = getUsers();
  const userIndex = users.findIndex(u => u.email.toLowerCase() === email.toLowerCase());

  if (userIndex === -1) {
    throw new AuthError('User not found');
  }

  users[userIndex].password = newPassword;
  saveUsers(users);
};

export const logout = (): void => {
  sessionStorage.removeItem('currentUser');
  sessionStorage.removeItem('token');
};

export const getCurrentUser = (): Omit<User, 'password'> | null => {
  const userJson = sessionStorage.getItem('currentUser');
  if (!userJson) return null;

  try {
    return JSON.parse(userJson);
  } catch {
    return null;
  }
};

export const isAuthenticated = (): boolean => {
  return !!(sessionStorage.getItem('token') && getCurrentUser());
};