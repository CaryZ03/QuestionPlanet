<template>
    
    <div class="container">
        <ul id="scene">
            <li class="layer" data-depth=".2"><img src="../assets/planet1.png"></li>
            <li class="layer" data-depth=".3"><img src="../assets/planet2.png"></li>
            <li class="layer" data-depth=".2"><img src="../assets/man.png"></li>
            <li class="layer" data-depth=".5"><img src="../assets/earth.png"></li>
            <li class="layer" data-depth=".1"><img src="../assets/text.png"></li>
            <li class="layer" data-depth=".4"><img src="../assets/planet3.png"></li>
            <li class="layer" data-depth=".8"><img src="../assets/planet4.png"></li>
            <li class="layer" data-depth="0"><img src="../assets/planet5.png"></li>
        </ul>
    </div>
    
</template>



<script >
import parallax from "../api/parallax.js"
const Parallax = window.Parallax; // 导入全局的 Parallax 构造函数


export default {
    mounted() {
            const scene = document.getElementById('scene');
            const parallax = new Parallax(scene);
        }
}

</script>

<style scoped>
    body {
    margin: 0;
    padding: 0;
}

.container {
    width: 100%;
    height: 100vh;
    overflow: hidden ;
    /* background:  url('../assets/homebackground.jpg'); */
    background-attachment: fixed;
    /* background-color: transparent; */
    position: relative;
    
    
    z-index: 500;
}
img{
    background: transparent;
}

ul{
    background-color: transparent;
}


</style>