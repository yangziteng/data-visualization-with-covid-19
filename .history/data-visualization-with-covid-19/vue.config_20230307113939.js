const isProduction = process.env.NODE_ENV === 'development';

module.exports = {
  publicPath: isProduction ? './' : '/',//为项目中的所有资源(js、css、img)指定一个基础路径
  devServer: {
    proxy: {
      '/': {//根据请求路径，匹配所有以/a开头的路径
        target: 'http://127.0.0.1:54526',//需要代理的服务器地址
        secure: false,  // 如果是https开头，要设置为true
        changeOrigin: true,  //为true时，发送请求头中的host会设置成target。为false，则不变。默认为true
        // pathRewrite: { '/api': '' },// 发送请求时，请求路径重写：将 /a/xxx --> /xxx （去掉/a）

      }
    },
    // port: '8080'//可自己修改端口
  },
}
