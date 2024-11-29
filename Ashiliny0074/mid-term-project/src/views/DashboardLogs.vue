<template>
  <div class="p-6">
    <div class="md:flex md:items-center md:justify-between mb-6">
      <h2 class="text-2xl font-bold text-gray-900">System Logs</h2>
      <div class="mt-4 flex space-x-3 md:mt-0">
        <select 
          v-model="filter" 
          class="rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
        >
          <option value="all">All Events</option>
          <option value="alert">Alerts</option>
          <option value="warning">Warnings</option>
          <option value="info">Info</option>
        </select>
        <button 
          @click="clearLogs"
          class="inline-flex items-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50"
        >
          Clear Logs
        </button>
        <button 
          @click="exportLogs"
          class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700"
        >
          Export Logs
        </button>
      </div>
    </div>

    <!-- Logs Table -->
    <div class="bg-white shadow overflow-hidden rounded-lg">
      <div class="min-w-full divide-y divide-gray-200">
        <div class="bg-white">
          <div class="max-h-[600px] overflow-auto">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50 sticky top-0">
                <tr>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Timestamp
                  </th>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Type
                  </th>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Message
                  </th>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Value
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="log in filteredLogs" :key="log.id" :class="getRowColor(log.type)">
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ formatDate(log.timestamp) }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span :class="getTypeClass(log.type)">
                      {{ log.type }}
                    </span>
                  </td>
                  <td class="px-6 py-4 text-sm text-gray-900">
                    {{ log.message }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ log.value }}
                  </td>
                </tr>
                <tr v-if="filteredLogs.length === 0">
                  <td colspan="4" class="px-6 py-4 text-center text-sm text-gray-500">
                    No logs found
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';

interface Log {
  id: number;
  timestamp: Date;
  type: 'info' | 'warning' | 'alert';
  message: string;
  value: string;
}

const filter = ref('all');
const logs = ref<Log[]>([]);

// Generate sample logs
const generateSampleLogs = () => {
  const sampleMessages = {
    temperature: [
      'Temperature above threshold',
      'Temperature below threshold',
      'Temperature normal',
    ],
    humidity: [
      'Humidity above threshold',
      'Humidity below threshold',
      'Humidity normal',
    ],
    soilMoisture: [
      'Soil moisture critical',
      'Soil moisture low',
      'Soil moisture optimal',
    ],
    lightLevel: [
      'Light level too high',
      'Light level too low',
      'Light level optimal',
    ],
  };

  const types: ('info' | 'warning' | 'alert')[] = ['info', 'warning', 'alert'];
  const now = new Date();
  const sampleLogs: Log[] = [];

  for (let i = 0; i < 50; i++) {
    const randomType = types[Math.floor(Math.random() * types.length)];
    const category = ['temperature', 'humidity', 'soilMoisture', 'lightLevel'][
      Math.floor(Math.random() * 4)
    ];
    const messages = sampleMessages[category as keyof typeof sampleMessages];
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    
    sampleLogs.push({
      id: i,
      timestamp: new Date(now.getTime() - Math.random() * 24 * 60 * 60 * 1000),
      type: randomType,
      message: randomMessage,
      value: randomType === 'info' 
        ? 'Normal range'
        : `${(20 + Math.random() * 10).toFixed(1)}°C`
    });
  }

  return sampleLogs.sort((a, b) => b.timestamp.getTime() - a.timestamp.getTime());
};

const filteredLogs = computed(() => {
  if (filter.value === 'all') return logs.value;
  return logs.value.filter(log => log.type === filter.value);
});

const formatDate = (date: Date) => {
  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'short',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  }).format(date);
};

const getTypeClass = (type: string) => {
  const baseClasses = 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full';
  switch (type) {
    case 'alert':
      return `${baseClasses} bg-red-100 text-red-800`;
    case 'warning':
      return `${baseClasses} bg-yellow-100 text-yellow-800`;
    default:
      return `${baseClasses} bg-green-100 text-green-800`;
  }
};

const getRowColor = (type: string) => {
  switch (type) {
    case 'alert':
      return 'bg-red-50 hover:bg-red-100';
    case 'warning':
      return 'bg-yellow-50 hover:bg-yellow-100';
    default:
      return 'hover:bg-gray-50';
  }
};

const exportLogs = () => {
  const data = JSON.stringify(filteredLogs.value, null, 2);
  const blob = new Blob([data], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `greenhouse-logs-${new Date().toISOString()}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
};

const clearLogs = () => {
  if (confirm('Are you sure you want to clear all logs?')) {
    logs.value = [];
  }
};

// Add new log entry
const addLog = (type: 'info' | 'warning' | 'alert', message: string, value: string) => {
  logs.value.unshift({
    id: Date.now(),
    timestamp: new Date(),
    type,
    message,
    value
  });
};

// Initialize logs
onMounted(() => {
  logs.value = generateSampleLogs();

  // Simulate real-time logs
  setInterval(() => {
    const types: ('info' | 'warning' | 'alert')[] = ['info', 'warning', 'alert'];
    const randomType = types[Math.floor(Math.random() * types.length)];
    const messages = [
      'Temperature check',
      'Humidity check',
      'Soil moisture check',
      'Light level check'
    ];
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    addLog(randomType, randomMessage, `${(20 + Math.random() * 10).toFixed(1)}°C`);
  }, 10000);
});
</script>
