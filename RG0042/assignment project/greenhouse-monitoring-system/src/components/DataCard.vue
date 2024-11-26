<template>
  <div class="card" :class="{ warning: exceedsThreshold }">
    <div class="card-header">
      <span class="icon">{{ icon }}</span>
      <span class="label">{{ label }}</span>
    </div>
    <div class="value">
      {{ value }} <span class="unit">{{ unit }}</span>
    </div>
    <div class="description">{{ description }}</div>
  </div>
</template>

<script>
export default {
  name: "DataCard",
  props: {
    label: {
      type: String,
      required: true,
    },
    unit: {
      type: String,
      default: "",
    },
    description: {
      type: String,
      default: "No description available.",
    },
    icon: {
      type: String,
      default: "ℹ️",
    },
    initialValue: {
      type: Number,
      default: 0,
    },
    min: {
      type: Number,
      default: 0,
    },
    max: {
      type: Number,
      default: 100,
    },
    warningThreshold: {
      type: Number,
      default: 80,
    },
  },
  data() {
    return {
      value: this.initialValue,
    };
  },
  computed: {
    exceedsThreshold() {
      return this.value > this.warningThreshold;
    },
  },
  methods: {
    updateValue() {
      this.value = parseFloat(
        (this.min + Math.random() * (this.max - this.min)).toFixed(1)
      );
    },
  },
  mounted() {
    this.updateInterval = setInterval(this.updateValue, 5000);
  },
  beforeUnmount() {
    clearInterval(this.updateInterval);
  },
};
</script>

<style scoped>
.card {
  background: linear-gradient(145deg, #ffffff, #f0f0f0);
  border-radius: 12px;
  box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.1), -4px -4px 10px rgba(255, 255, 255, 0.8);
  text-align: center;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 6px 6px 15px rgba(0, 0, 0, 0.2), -6px -6px 15px rgba(255, 255, 255, 0.8);
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-size: 1.2rem;
  font-weight: bold;
  color: #34495e;
}

.icon {
  font-size: 2rem;
}

.value {
  font-size: 2.5rem;
  font-weight: 700;
  color: #2c3e50;
}

.unit {
  font-size: 1.2rem;
  font-weight: 500;
  color: #777;
}

.description {
  font-size: 1rem;
  font-weight: 500;
  color: #666;
}

.card.warning {
  background: linear-gradient(145deg, #ffeaea, #ffdcdc);
  border-color: #d80000;
}

.card.warning .value {
  color: #d80000;
}
</style>