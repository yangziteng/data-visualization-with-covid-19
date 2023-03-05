let baseUrl = 'http://127.0.0.1:8000'
if (process.env.NODE_ENV === 'development') {
  baseUrl = 'http://127.0.0.1:8000'
} else {
  // 你的 API 地址
  baseUrl = 'http://127.0.0.1:8000'
}

export default {
  baseUrl
}