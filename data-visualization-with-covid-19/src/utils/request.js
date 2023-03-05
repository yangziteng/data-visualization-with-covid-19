import axios from "axios"
import sysConst from '../libs/const'
const fetch = (method = 'GET', url, param = '') => {
  // 处理 url
  // url = `${sysConst.baseUrl}${url}`

  console.log(url)
  return new Promise((resolve, reject) => {
    axios({
      method: method,
      changeOrigin: true, //可否跨域
      url: url,
      // changeOrigin: true,
      data: JSON.stringify(param)
    }).then((res) => {
      console.log("成功")
      resolve(res.data)
    }, error => {
      reject(error)
      console.log("失败")
    }).catch((error) => {
      reject(error)
    })
  })
}

const get = (url) => {
  return fetch('GET', url)
}

const post = (url, data) => {
  return fetch('POST', url, data)
}

const put = (url, data) => {
  return fetch('PUT', url, data)
}

const remove = (url, data) => {
  return fetch('DELETE', url, data)
}

export {
  get,
  post,
  put,
  remove
}