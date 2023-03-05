import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: () => import('@/views/main-layout')
  },
  {
    path: '/world',
    name: 'World',
    component: () => import('@/views/main-world-layout')
  }
]

const router = new Router({
  routes: routes
})

export default router