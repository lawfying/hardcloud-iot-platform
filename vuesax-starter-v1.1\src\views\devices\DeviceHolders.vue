<template>
  <div class="mt-5">

    <vs-row>


    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="5">
        <vs-input placeholder="搜索设备名称或者持有人名称" v-model="knowledgeBaseSearchQuery"  icon-pack="feather" icon="icon-search"  class="w-full no-icon-border mt-4" />
    </vs-col>

    </vs-row>

        <vs-divider/>

 
  <vs-table pagination max-items="10" :data="filteredKB" stripe>

    <template slot="thead">
      <!-- <vs-th>序号</vs-th> -->
      <vs-th>持有的设备</vs-th>
      <vs-th>设备持有人</vs-th>
      
      <vs-th>设备ID</vs-th>
      <vs-th>绑定时间</vs-th>

    </template>

    <template slot-scope="{data}">
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
        
        <!-- <vs-td :data="data[indextr].id">
          {{ indextr+1 }}
        </vs-td> -->

        <vs-td :data="data[indextr].holddevice">
         {{ data[indextr].holddevice }}
        </vs-td>

        <vs-td :data="data[indextr].holder">
        {{ data[indextr].holder }}
        </vs-td>

        <vs-td :data="data[indextr].holddevid">
         {{ data[indextr].holddevid }}
        </vs-td>


        <vs-td :data="data[indextr].holddate">
          {{ data[indextr].holddate | formatDate }}
        </vs-td>

      

      </vs-tr>
    </template>
  </vs-table>
  </div>

</template>

<script>

var padDate = function(va){
  va=va<10?'0'+va:va;
  return va
}

import {FormWizard, TabContent} from 'vue-form-wizard'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
import vSelect from 'vue-select'

export default {


  data() {
    return {
     
      holddevices:[],
      url:this.GLOBAL.baseURL,
      knowledgeBaseSearchQuery: '',

      
    }
  },
  computed: {
		filteredKB() { 
			return this.holddevices.filter((item) => item.holder.toLowerCase().includes(this.knowledgeBaseSearchQuery.toLowerCase()) || item.holddevice.toLowerCase().includes(this.knowledgeBaseSearchQuery.toLowerCase()));
    }
    
    },
    

  created: async function() {
      const response = await this.axios.get(this.GLOBAL.baseURL+'/rest-auth/devholder/holddevlist/').catch(function (error) {
			console.log(error)
            return error.response.data;});
      if (response.status==200) {
          this.holddevices = response.data;
      }


  },

  filters:{
        formatDate:function (val) {
            var value=new Date(val);
            var year=value.getFullYear();
            var month=padDate(value.getMonth()+1);
            var day=padDate(value.getDate());
            var hour=padDate(value.getHours());
            var minutes=padDate(value.getMinutes());
            var seconds=padDate(value.getSeconds());
            return year+'-'+month+'-'+day+' '+hour+':'+minutes+':'+seconds;
 
        }
    },


	components: {
		'v-select': vSelect,
		FormWizard,
		TabContent
	}
  


}
</script>