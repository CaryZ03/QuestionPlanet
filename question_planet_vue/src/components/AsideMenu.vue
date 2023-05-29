<template>
    <body>
        <div class="wrap">
            <div class="nav">
                <!--按钮-->
                <div class="btn">
                    <div class="btn-item"></div>
                    <div class="btn-item"></div>
                    <div class="btn-item"></div>
                </div>
                <!--头像-->
                <div class="icon">
                    <div class="icon-img"><img src="../assets/background.png" alt="" /></div>
                    <div class="icon-con">
                        <p>Good Day</p>
                        <h2>Vitaliy D.</h2>
                    </div>
                </div>
                <div class="line"></div>
                <div class="title">
                    <p>Menu 6</p>
                </div>
                <div class="menu">
                    <div class="item">
                        <div class="light"></div>
                        <div class="licon"><span class="iconfont icon-wenjian"></span></div>
                        <div class="con" @click="createNewQ">从空白创建</div>
                        <div class="ricon"><span class="iconfont icon-shezhi"></span></div>
                    </div>
                    <div class="item">
                        <div class="light"></div>
                        <div class="licon"><span class="iconfont icon-qipao1"></span></div>
                        <div class="con">Products</div>
                        <div class="ricon"></div>
                    </div>
                    <div class="item">
                        <div class="light"></div>
                        <div class="licon">
                            <span class="iconfont icon-xiaolian"></span>
                        </div>
                        <div class="con">Sales</div>
                        <div class="ricon"><span class="iconfont icon-caidan1"></span></div>
                    </div>
                    <div class="item">
                        <div class="light"></div>
                        <div class="licon">
                            <span class="iconfont icon-shexiang"></span>
                        </div>
                        <div class="con">Discount</div>
                        <div class="ricon"></div>
                    </div>
                    <div class="item">
                        <div class="light"></div>
                        <div class="licon">
                            <span class="iconfont icon-wenjian1"></span>
                        </div>
                        <div class="con">Payouts</div>
                        <div class="ricon"></div>
                    </div>
                </div>
                <div class="line"></div>
                <div class="title">
                    <p>Sever 6</p>
                </div>
                <div class="serve">
                    <div class="item">
                        <div class="licon"><span class="iconfont icon-caidan"></span></div>
                        <div class="con">Software</div>
                        <div class="ricon">
                            <span class="iconfont icon-Dashboard"></span>
                        </div>
                    </div>
                    <div class="item">
                        <div class="licon"><span class="iconfont icon-renqun"></span></div>
                        <div class="con">Chat</div>
                        <div class="ricon"></div>
                    </div>
                    <div class="item">
                        <div class="licon"><span class="iconfont icon-sousuo"></span></div>
                        <div class="con">Intercom</div>
                        <div class="ricon"><span class="iconfont icon-caidan1"></span></div>
                    </div>
                    <div class="item">
                        <div class="licon">
                            <span class="iconfont icon-gengduo-a"></span>
                        </div>
                        <div class="con">Setting</div>
                        <div class="ricon"></div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</template>

<script>
export default {
    data() {
        return {

        }
    },
    methods: {
        createNewQ(){
            const data={
                "uid": this.$store.state.curUserID
            }
            console.log(data)
            this.$api.questionnaire.postQuestionnaire_Create(data).then((res)=>{
                console.log(res.data.errno+res.data.qn_id)
            }).catch((err)=>{
                console.log(err)
            })
        }

    },

}
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    color: rgba(255, 255, 255, 0.6);
}

.wrap {
    width: 100%;
    height: 70vh;


    /* background: url(img/bg.jpg) center no-repeat; */
    background-size: cover;
    display: flex;
    align-items: center;
    justify-content: center;

    transform: scale(0.8);
}

.nav {
    background-color: rgba(0, 0, 0, 0.8);
    border-radius: 20px;
    box-sizing: border-box;
    color: rgba(255, 255, 255, 0.6);
    font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
    font-size: 12px;
    height: 820px;
    overflow: hidden;
    padding: 0;
    text-align: left;
    top: 15%;
    transition: all .5s;
    width: 110px;
    margin: 0 180px -119px -144px;
    transition: 0.5s;
}

.nav:hover {
    width: 280px;
}

.btn {
    width: 60px;
    height: 10px;
    display: flex;
    justify-content: space-around;
    margin-left: 25px;
    margin-top: 25px;
}

.btn-item {
    width: 10px;
    height: 10px;
    border-radius: 50%;
}

.btn-item:nth-child(1) {
    background: #eb5a56;
}

.btn-item:nth-child(2) {
    background: #f8bc33;
}

.btn-item:nth-child(3) {
    background: #62cb44;
}

.icon {
    width: 250px;
    height: 60px;
    margin-left: 25px;
    margin-top: 20px;
    display: flex;
}

.icon-img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 4px solid rgba(255, 255, 255, 0.3);
    overflow: hidden;
}

.icon-img img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

.icon-con {
    height: 60px;
    margin-left: 25px;
}

.icon-con p {
    padding-top: 5px;
}

.icon-con h2 {
    font-weight: 400;
}

.line {
    width: 60px;
    height: 1px;
    background: rgba(245, 253, 255, 0.5);
    margin: 20px 25px;
    transition: 0.5s;
}

.nav:hover .line {
    width: 230px;
}

.title {
    width: 60px;
    margin-left: 25px;
    margin-bottom: 20px;
}

.title p {
    font-size: 14px;
}

.menu {
    width: 230px;
    margin-left: 25px;
}

.item {
    display: flex;
    position: relative;
    transition: 0.5s;
    border-radius: 6px;
}

.item:hover {
    background: rgba(255, 255, 255, 0.1);
}

.licon {
    width: 60px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.con {
    width: 0px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: 0.5s;
    overflow: hidden;
    position: relative;
    left: -20px;
    opacity: 0;
}

.nav:hover .con {
    width: 160px;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 1;
}

.ricon {
    width: 0px;
    height: 50px;
    transition: 0.5s;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    opacity: 0;
}

.nav:hover .ricon {
    width: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 1;
}

.iconfont {
    font-size: 26px;
}

.ricon .iconfont {
    font-size: 20px;
    color: #62cb44;
}

.light {
    width: 6px;
    height: 50px;
    background: #eb5a56;
    position: absolute;
    left: -25px;
    transition: 0.5s;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    opacity: 0;
}

.item:hover .light {
    opacity: 1;
}

.serve {
    width: 60px;
    /*    background: rgba(98, 203, 68, 0.5);*/
    background: rgba(0, 0, 0, 0.7);
    margin-left: 25px;
    border-radius: 10px;
    overflow: hidden;
    transition: 0.5s;
}

.nav:hover .serve {
    width: 230px;
}

/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
/*占位*/
</style>