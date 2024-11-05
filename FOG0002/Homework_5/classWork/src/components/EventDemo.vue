<script setup>
import {ref} from 'vue';

const clickHandelBox=()=>{
    alert("Div Clicked");
}

const clickHandelBtn=()=>{
    alert("BTN clicked");
}

</script>

<template>
    <div>
        <div class="box" @click="clickHandelBox">
            <div class="btn">
                <button @click.stop="clickHandelBtn">BTN</button>
            </div>
            <div class="btn" @click.stop="">
                <router-link to="/expression-demo" id="btnStyle">Go to 3rd homework</router-link>
            </div>

        </div>
    </div>
</template>

<style scoped>
    div{
        background: rgb(134, 248, 134);
        width: 800px;
        height: 800px;
        display: flex;
        justify-content: center;        
    }
    .box h1{
        display: flex;
        justify-content: center;
    }
    .btn{
        display: flex;
        align-items: center;
        justify-content: center;
    }

    button {
        width: 40%;
        padding: 10px;
        background-color: #0f4550;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }
      
      button:hover {
        background-color: #4186c6;
      }

      #btnStyle {
        width: 40%;
        padding: 10px;
        background-color: #0f4550;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }
      
      #btnStyle:hover {
        background-color: #4186c6;
      }
</style>