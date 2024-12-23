<template>
  <div>
    <h2>Toggle Visibility Demo</h2>
    <button @click="toggleMessageVisibility">Toggle Visibility</button>

    <div v-if="isMessageVisible">This message is shown when using v-if</div>
    
    <div v-show="isMessageVisible">This message is shown when using v-show</div>
  </div>
</template>

<script>
export default {
  name: 'VisibilityToggler', 
  
  data() {
    return {
      isMessageVisible: false 
    };
  },

  methods: {
    toggleMessageVisibility() {
      this.isMessageVisible = !this.isMessageVisible;
    }
  }
};
</script>

<style scoped>
button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

div {
  margin-top: 10px;
  font-size: 18px;
  color: #333;
}
</style>
