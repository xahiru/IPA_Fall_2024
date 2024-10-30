<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment() {
  count.value++
}

console.log(count) // { value: 0 } 
console.log(count.value) // 0 
count.value++
 console.log(count.value) 


</script>

<template>
  <button @click="count++">
    {{ count }}
  </button>
  <!-- <button @click="increment">
    {{ count }}
  </button> -->
</template>