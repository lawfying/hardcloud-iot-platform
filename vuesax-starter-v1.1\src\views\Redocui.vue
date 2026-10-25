<template>
  <div>
	redoc格式HTTP接口。
  </div>
  </template>

<script>


export default {


  data() {
    return {

      url:this.GLOBAL.baseURL,

    }
  },

  mounted: function() {
	//window.open(this.url+'/redoc/', '_blank');
	window.location.href = this.url+'/redoc/';
  },  



}
</script>