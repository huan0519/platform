<template>
  <button
      :class="['interactive-button', { 'is-loading': loading }]"
      :disabled="loading || disabled"
      @click="handleClick"
  >
    <span v-if="!loading">{{ label }}</span>
    <span v-else class="loading-spinner"></span>
  </button>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      default: 'Click Me',
    },
    loading: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    handleClick() {
      this.$emit('click');
    },
  },
};
</script>

<style scoped>
.interactive-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75em 1.5em;
  font-size: 16px;
  font-weight: bold;
  color: #fff;
  background-color: #2563eb;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.interactive-button:hover {
  background-color: #1d4ed8;
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}

.interactive-button:active {
  background-color: #1e40af;
  transform: translateY(0);
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.1);
}

.interactive-button.is-loading {
  cursor: not-allowed;
}

.interactive-button .loading-spinner {
  width: 20px;
  height: 20px;
  border: 3px solid transparent;
  border-top: 3px solid #fff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
