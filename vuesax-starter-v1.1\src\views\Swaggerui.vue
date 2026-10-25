<template>
  <div>
	Swagger格式HTTP接口。
  </div>
  </template>

<script>


export default {


  data() {
    return {

      url:this.GLOBAL.baseURL,

    }
  },

  created: function() {
	//window.open(this.url+'/docs/');
	window.location.href = this.url+'/docs/';
  },  



}
</script>