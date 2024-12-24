<template>
    <div class="math-demo">
        <div class="inputs">
        <div>
            <label>Number 1:</label>
            <input type="number" v-model.number="num1">
        </div>
        <div>
            <label>Number 2:</label>
            <input type="number" v-model.number="num2">
            </div>
        </div>

        <div class="results">
            <p>The sumof{{ num1 }} and {{ num2 }} is:{{ num1+num2 }}</p>
            <p>The difference is:{{ num1-num2 }}</p>
            <p>The product is:{{ num1*num2 }}</p>
            <p>The quotient is:{{ num1/num2 }}</p>
        </div>
    </div>
</template>

<script>
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
    setup() {
        
    },
})
</script>

<style scoped>
.math-demo {
    padding:20px;
    max-width:400px;
    margin:0 auto;
}

.inputs{
    margin-bottom: 20px;
}

.inputs div {
    margin: 10px0;
}

label{
    display: inline-block;
    width: 100px;
}

input {
    padding: 5px;
    width: 100px;
}

.results {
    background: #f5f5f5;
    padding: 15px;
    border-radius: 5px;
}

.results p {
    margin: 10px0;
}
</style>