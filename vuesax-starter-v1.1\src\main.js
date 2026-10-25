/*=========================================================================================
  File Name: main.js
  Description: main vue(js) file
  ----------------------------------------------------------------------------------------
  Item Name: Vuesax Admin - VueJS Dashboard Admin Template
  Version: 1.1
  Author: Pixinvent
  Author URL: hhttp://www.themeforest.net/user/pixinvent
==========================================================================================*/


import Vue from 'vue'
import App from './App.vue'

// Vuesax Component Framework
import Vuesax from 'vuesax'
import 'material-icons/iconfont/material-icons.css' //Material Icons
import 'vuesax/dist/vuesax.css' // Vuesax
import globalVariable from '@/globalVariable'
import globalFunction from '@/globalFunction'

Vue.prototype.GLOBAL = globalVariable
Vue.use(Vuesax)
Vue.use(globalFunction)

import axios from 'axios'

Vue.prototype.axios = axios


// Theme Configurations
import '../themeConfig.js'

// Globally Registered Components
import './globalComponents.js'

// Styles: SCSS
import './assets/scss/main.scss'

// Tailwind
import '@/assets/css/main.css';

// Vue Router
import router from './router'


// Vuex Store
import store from './store/store'

// PrismJS
import 'prismjs'
import 'prismjs/themes/prism.css'



// Feather font icon
require('./assets/css/iconfont.css')

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    const accessToken = window.sessionStorage.getItem('Authorization')
    if (!accessToken) {
      next({
        path: '/pages/login',
        query: { redirect: to.fullPath }//把要跳转的地址作为参数传到下一步
      })
    } else {
      next()
    }
  } else {
    next() // 确保一定要调用 next()
  }
})

// 添加请求拦截器
axios.interceptors.request.use(function (config) {

  config.headers['Authorization'] = window.sessionStorage.getItem('Authorization')
  return config

  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error)
  });

/*
// 添加响应拦截器
axios.interceptors.response.use(function (response) {
  // 对响应数据做点什么
  return response
}, function (error) {
  // 对响应错误做点什么
  return Promise.reject(error)
});
*/
new Vue({
  router,
  store,
  render: h => h(App)
  
}).$mount('#app')