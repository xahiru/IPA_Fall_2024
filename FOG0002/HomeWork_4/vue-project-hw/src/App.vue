<script setup>
import ToggleVisibility from './components/ToggleVisibility.vue';
import { ref } from 'vue';

const isActive = ref(true);
const handleClick=()=>{
  isActive.value= !isActive.value
    // if(isActive.value==true){
    //   isActive.value=false
    // }
    // else{
    //   isActive.value=true
    // }
}
</script>

<template>
  <div >
    <button @click="handleClick">BTN</button>

    <div v-if="isActive">
      <ToggleVisibility />
    </div>
  </div>
</template>

<style scoped>
</style>
