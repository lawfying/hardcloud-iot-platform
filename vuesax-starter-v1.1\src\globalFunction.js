//全局函数，当用户登录时获取access token,
// param为传入参数
//导入全局变量
import globalVariable from '@/globalVariable'

import axios from 'axios'

//用户登录时，生成token，保存在全局变量中,需要调用http://127.0.0.1:8000/token-api/token/
async function tokenFunction (params) {
  //alert('tokenfunction000')
  const response = await axios.post(globalVariable.baseURL+'/token-api/token/',params)
  console.log(response)
  //alert('tokenfunction')
  window.sessionStorage.setItem('Authorization', 'Bearer'+' '+ response.data.access)
  window.sessionStorage.setItem('accessToken', response.data.access)
  window.sessionStorage.setItem('refreshToken', response.data.refresh)

}
/*
function tokenFunction (params) {

  axios.post(globalVariable.baseURL+'/token-api/token/',params).then(function (response) {
    globalVariable.accessToken = response.data.access;
    globalVariable.refreshToken = response.data.refresh;
    console.log(response);
  }).catch(function (error) {
    //return JSON.stringify(error.response.data);
    console.log(error);
});
}
*/

//调用需要accesstoken的API，首先判断accesstoken是否有效，如果无效，采用refreshtoken重新生成新的accesstoken
//需要调用http://127.0.0.1:8000/token-api/token/refresh/

function refreshFunction () {
  const refreshToken=window.sessionStorage.getItem('refreshToken')
  var params = {refresh:refreshToken}
  axios.post(globalVariable.baseURL+'/token-api/token/refresh/',params).then(function (response) {
    window.sessionStorage.setItem('accessToken', response.data.access)
    console.log(response)
  }).catch(function (error) {
    console.log(error);
  });
    
  }

  export default {
    // Vue.js的插件应当有一个公开方法 install。这个方法的第一个参数是 Vue 构造器，第二个参数是一个可选的选项对象。
    install: function (Vue) {
      Vue.prototype.tokenFunction = (param) => tokenFunction(param);
      Vue.prototype.refreshFunction = (param) => refreshFunction(param);
    }
  }