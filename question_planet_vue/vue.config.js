const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  // chainWebpack: (config) => {
  //   // 禁止 image-webpack-loader 自动填充 PNG 图片的透明背景
  //   config.module.rule('images').use('image-webpack-loader').tap(options => ({
  //     ...options,
  //     background: false,
  //   }));
  // }
})
