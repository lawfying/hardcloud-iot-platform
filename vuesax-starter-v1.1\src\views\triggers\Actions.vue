<template>
  <div class="mt-5">
    <vs-tabs vs-alignment="fixed">
      <vs-tab vs-label="HTTP协议动作">
        <vs-row>
          <div class="w-full sm:w-1/2 md:w-3/4 px-2">
            <vx-card class="overlay-card overflow-hidden">
              <br />
              <vs-row>
                <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="2">
                  <vs-input class="inputx w-full" placeholder="动作名称" v-model="globalact_title" />
                </vs-col>
                <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="6">
                  <vs-input class="inputx w-full" placeholder="动作URL" v-model="globalact_url" />
                </vs-col>
                <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                  <vs-button
                    color="success"
                    type="flat"
                    icon-pack="feather"
                    icon="icon-plus"
                    v-on:click="addglobalhttpaction()"
                  >添加HTTP动作</vs-button>
                </vs-col>
              </vs-row>
              <br />
              <vs-divider />
              <br />
              <vs-table max-items="10" pagination :data="globalhttpactionList">
                <template slot="thead">
                  <vs-th>ID</vs-th>
                  <vs-th>动作名称</vs-th>
                  <vs-th>动作URL</vs-th>
                  <vs-th style="padding-left:60px;">操作</vs-th>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                    <vs-td :data="data[indextag].id">{{ data[indextag].id }}</vs-td>

                    <vs-td :data="data[indextag].title">{{ data[indextag].title }}</vs-td>

                    <vs-td :data="data[indextag].url">{{ data[indextag].url }}</vs-td>
                    <vs-td style="width:200px;">
                      <vs-row>
                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                          <span class="text-success">
                            <vx-tooltip color="primary" text="参数管理">
                              <vs-button
                                radius
                                color="success"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-file-text"
                                v-on:click="show_actionparams(tag)"
                              ></vs-button>
                            </vx-tooltip>
                          </span>
                        </vs-col>

                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                          <span class="text-success">
                            <vx-tooltip color="primary" text="编辑">
                              <vs-button
                                radius
                                color="success"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-edit-2"
                                @click="popupActiveHttpact_updatefunc(tag)"
                              ></vs-button>
                              <vs-popup
                                class="holamundo"
                                title="编辑HTT动作"
                                :active.sync="popupActiveHttpact_update"
                                background-color="rgba(0,0,0,.1)"
                              >
                                <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">动作名称：</vs-col>
                                <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                  <vs-input class="inputx" v-model="globalhttpaction_title_tmp" />
                                </vs-col>
                                <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">动作URL：</vs-col>
                                <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                  <vs-textarea class="inputx" v-model="globalhttpaction_url_tmp" />
                                </vs-col>
                                <br />
                                <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                  <vs-button
                                    color="success"
                                    type="border"
                                    @click="globalhttpaction_update(globalhttpaction_id_tmp)"
                                  >更新</vs-button>
                                </vs-col>
                              </vs-popup>
                            </vx-tooltip>
                          </span>
                        </vs-col>

                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                          <span class="text-danger">
                            <vx-tooltip color="danger" text="删除">
                              <vs-button
                                radius
                                color="danger"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-trash"
                                @click="popupActiveHttpact_delfunc(tag)"
                              ></vs-button>
                              <vs-popup
                                class="holamundo"
                                title="删除HTTP动作"
                                :active.sync="popupActiveHttpact_del"
                                background-color="rgba(0,0,0,.1)"
                              >
                                <vs-row vs-justify="center">
                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="danger"
                                      type="filled"
                                      @click="delglobalhttpact(globalhttpaction_id_tmp)"
                                    >确认删除</vs-button>
                                  </vs-col>
                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="warning"
                                      type="filled"
                                      @click="popupActiveHttpact_del=false"
                                    >取消</vs-button>
                                  </vs-col>
                                </vs-row>
                              </vs-popup>
                            </vx-tooltip>
                          </span>
                        </vs-col>
                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                <span class="text-success">
                                  <vx-tooltip color="primary" text="测试HTTP动作状态">
                                    <vs-button
                                      radius
                                      color="success"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-refresh-ccw"
                                      v-on:click="test_actionstatus(tag)"
                                    ></vs-button>
                                  </vx-tooltip>
                                </span>
                              </vs-col>
                      </vs-row>
                    </vs-td>
                  </vs-tr>
                </template>
              </vs-table>
            </vx-card>
          </div>

          <div class="w-full sm:w-1/2 md:w-1/4 px-2" v-show="showactionparams">
            <vx-card class="overlay-card overflow-hidden">
              <h5>所属动作名称：{{ globalhttpaction_title }}</h5>
              <vs-divider />
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                <vs-input class="inputx" placeholder="参数key" v-model="httpactparamKey" />
              </vs-col>
              <vs-row>
                <br />
              </vs-row>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                <vs-input class="inputx" placeholder="参数value" v-model="httpactparamValue" />
              </vs-col>
              <vs-row>
                <br />
              </vs-row>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                <vs-button
                  color="success"
                  type="border"
                  v-on:click="addhttpactparam(globalhttpaction_id)"
                >添加</vs-button>
              </vs-col>
              <vs-row>
                <br />
              </vs-row>

              <vs-divider>参数列表</vs-divider>

              <vs-table max-items="5" pagination :data="httpactparamList">
                <template slot="thead">
                  <vs-th>ID</vs-th>
                  <vs-th>KEY</vs-th>
                  <vs-th>VALUE</vs-th>
                  <vs-th style="padding-left:40px;">操作</vs-th>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                    <vs-td :data="data[indextr].id">{{ data[indextr].id }}</vs-td>
                    <vs-td :data="data[indextr].key">{{ data[indextr].key }}</vs-td>

                    <vs-td :data="data[indextr].value">{{ data[indextr].value }}</vs-td>

                    <vs-td>
                      <vs-row>
                        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                          <span class="text-danger">
                            <vx-tooltip color="danger" text="删除">
                              <vs-button
                                radius
                                color="danger"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-trash"
                                @click="popupActiveActparam_func(tr)"
                              ></vs-button>
                              <vs-popup
                                class="holamundo"
                                title="删除动作参数"
                                :active.sync="popupActiveActparam_del"
                                background-color="rgba(0,0,0,.1)"
                              >
                                <vs-row vs-justify="center">
                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="danger"
                                      type="filled"
                                      @click="delactparam(httpactparam_id)"
                                    >确认删除</vs-button>
                                  </vs-col>

                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="warning"
                                      type="filled"
                                      @click="popupActiveActparam_del=false"
                                    >取消</vs-button>
                                  </vs-col>
                                </vs-row>
                              </vs-popup>
                            </vx-tooltip>
                          </span>
                        </vs-col>
                      </vs-row>
                    </vs-td>
                  </vs-tr>
                </template>
              </vs-table>
            </vx-card>
          </div>
        </vs-row>
      </vs-tab>
      <vs-tab vs-label="MQTT协议动作" @click="init_mqtt_action()">
        <vs-row>
          <div class="w-full sm:w-1/2 md:w-3/4 px-2">
            <vx-card class="overlay-card overflow-hidden">
              <br />
              <vs-row>
                <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="2">
                  <vs-input
                    class="inputx w-full"
                    placeholder="MQTT动作名称"
                    v-model="global_mqtt_act_title"
                  />
                </vs-col>
                <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="6">
                  <vs-input
                    class="inputx w-full"
                    placeholder="主题topic"
                    v-model="global_mqtt_topic"
                  />
                </vs-col>
                <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                  <vs-button
                    color="success"
                    type="flat"
                    icon-pack="feather"
                    icon="icon-plus"
                    v-on:click="addglobalmqttaction()"
                  >添加MQTT动作</vs-button>
                </vs-col>
              </vs-row>
              <br />
              <vs-divider />
              <br />
              <vs-table max-items="10" pagination :data="globalmqttactionList">
                <template slot="thead">
                  <vs-th>ID</vs-th>
                  <vs-th>MQTT动作名称</vs-th>
                  <vs-th>MQTT Topic</vs-th>
                  <vs-th style="padding-left:60px;">操作</vs-th>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                    <vs-td :data="data[indextag].id">{{ data[indextag].id }}</vs-td>

                    <vs-td :data="data[indextag].title">{{ data[indextag].title }}</vs-td>

                    <vs-td :data="data[indextag].topic">{{ data[indextag].topic }}</vs-td>
                    <vs-td style="width:200px;">
                      <vs-row>
                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                          <span class="text-success">
                            <vx-tooltip color="primary" text="参数管理">
                              <vs-button
                                radius
                                color="success"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-file-text"
                                v-on:click="show_mqttactionparams(tag)"
                              ></vs-button>
                            </vx-tooltip>
                          </span>
                        </vs-col>

                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                          <span class="text-success">
                            <vx-tooltip color="primary" text="编辑">
                              <vs-button
                                radius
                                color="success"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-edit-2"
                                @click="popupActiveMqttact_updatefunc(tag)"
                              ></vs-button>
                              <vs-popup
                                class="holamundo"
                                title="编辑MQTT动作"
                                :active.sync="popupActiveMqttact_update"
                                background-color="rgba(0,0,0,.1)"
                              >
                                <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">MQTT动作名称：</vs-col>
                                <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                  <vs-input class="inputx" v-model="globalmqttaction_title_tmp" />
                                </vs-col>
                                <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">MQTT Topic：</vs-col>
                                <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                  <vs-textarea class="inputx" v-model="globalmqttaction_topic_tmp" />
                                </vs-col>
                                <br />
                                <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                  <vs-button
                                    color="success"
                                    type="border"
                                    @click="globalmqttaction_update(globalmqttaction_id_tmp)"
                                  >更新</vs-button>
                                </vs-col>
                              </vs-popup>
                            </vx-tooltip>
                          </span>
                        </vs-col>

                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                          <span class="text-danger">
                            <vx-tooltip color="danger" text="删除">
                              <vs-button
                                radius
                                color="danger"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-trash"
                                @click="popupActiveMqttpact_delfunc(tag)"
                              ></vs-button>
                              <vs-popup
                                class="holamundo"
                                title="删除MQTT动作"
                                :active.sync="popupActiveMqttact_del"
                                background-color="rgba(0,0,0,.1)"
                              >
                                <vs-row vs-justify="center">
                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="danger"
                                      type="filled"
                                      @click="delglobalmqttact(globalmqttaction_id_tmp)"
                                    >确认删除</vs-button>
                                  </vs-col>
                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="warning"
                                      type="filled"
                                      @click="popupActiveMqttact_del=false"
                                    >取消</vs-button>
                                  </vs-col>
                                </vs-row>
                              </vs-popup>
                            </vx-tooltip>
                          </span>
                        </vs-col>
                      </vs-row>
                    </vs-td>
                  </vs-tr>
                </template>
              </vs-table>
            </vx-card>
          </div>

          <div class="w-full sm:w-1/2 md:w-1/4 px-2" v-show="showmqttactionparams">
            <vx-card class="overlay-card overflow-hidden">
              <h5>所属动作名称：{{ globalmqttaction_title }}</h5>
              <vs-divider />
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                <vs-input class="inputx" placeholder="参数key" v-model="mqttactparamKey" />
              </vs-col>
              <vs-row>
                <br />
              </vs-row>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                <vs-input class="inputx" placeholder="参数value" v-model="mqttactparamValue" />
              </vs-col>
              <vs-row>
                <br />
              </vs-row>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                <vs-button
                  color="success"
                  type="border"
                  v-on:click="addmqttactparam(globalmqttaction_id)"
                >添加</vs-button>
              </vs-col>
              <vs-row>
                <br />
              </vs-row>

              <vs-divider>参数列表</vs-divider>

              <vs-table max-items="5" pagination :data="mqttactparamList">
                <template slot="thead">
                  <vs-th>ID</vs-th>
                  <vs-th>KEY</vs-th>
                  <vs-th>VALUE</vs-th>
                  <vs-th style="padding-left:40px;">操作</vs-th>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                    <vs-td :data="data[indextr].id">{{ data[indextr].id }}</vs-td>
                    <vs-td :data="data[indextr].key">{{ data[indextr].key }}</vs-td>

                    <vs-td :data="data[indextr].value">{{ data[indextr].value }}</vs-td>

                    <vs-td>
                      <vs-row>
                        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                          <span class="text-danger">
                            <vx-tooltip color="danger" text="删除">
                              <vs-button
                                radius
                                color="danger"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-trash"
                                @click="popupActiveMqttActparam_func(tr)"
                              ></vs-button>
                              <vs-popup
                                class="holamundo"
                                title="删除动作参数"
                                :active.sync="popupActiveMqttActparam_del"
                                background-color="rgba(0,0,0,.1)"
                              >
                                <vs-row vs-justify="center">
                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="danger"
                                      type="filled"
                                      @click="delmqttactparam(mqttactparam_id)"
                                    >确认删除</vs-button>
                                  </vs-col>

                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="warning"
                                      type="filled"
                                      @click="popupActiveMqttActparam_del=false"
                                    >取消</vs-button>
                                  </vs-col>
                                </vs-row>
                              </vs-popup>
                            </vx-tooltip>
                          </span>
                        </vs-col>
                      </vs-row>
                    </vs-td>
                  </vs-tr>
                </template>
              </vs-table>
            </vx-card>
          </div>
        </vs-row>
      </vs-tab>
    </vs-tabs>
  </div>
</template>

<script>
var padDate = function(va) {
  va = va < 10 ? "0" + va : va;
  return va;
};

import vSelect from "vue-select";

export default {
  data() {
    return {
      globalhttpactionList: [],
      showactionparams: false,
      globalact_title: "",
      globalact_url: "",
      popupActiveHttpact_update: false,
      globalhttpaction_id: "",
      globalhttpaction_title: "",
      globalhttpaction_id_tmp: "",
      globalhttpaction_title_tmp: "",
      globalhttpaction_url_tmp: "",
      popupActiveHttpact_del: false,

      httpactparamList: [],
      httpactparamKey: "",
      httpactparamValue: "",
      popupActiveActparam_del: false,
      httpactparam_id: "",
      //以下是MQTT动作数据
      globalmqttactionList: [],
      global_mqtt_act_title: "",
      global_mqtt_topic: "",
      popupActiveMqttact_del: false,
      globalmqttaction_id_tmp: "",

      popupActiveMqttact_update: false,
      globalmqttaction_title_tmp: "",
      globalmqttaction_topic_tmp: "",
      showmqttactionparams: false,
      globalmqttaction_id: "",
      globalmqttaction_title: "",
      mqttactparamList: [],
      mqttactparamKey: "",
      mqttactparamValue: "",
      popupActiveMqttActparam_del: false
    };
  },
  mounted: async function() {
    const response = await this.axios
      .get(this.GLOBAL.baseURL + "/trigger/globalhttpaction/")
      .catch(function(error) {
        console.log(error);
        return error.response.data;
      });
    console.log(response);
    this.globalhttpactionList = response.data;
  },
  filters: {
    formatDate: function(val) {
      var value = new Date(val);
      var year = value.getFullYear();
      var month = padDate(value.getMonth() + 1);
      var day = padDate(value.getDate());
      var hour = padDate(value.getHours());
      var minutes = padDate(value.getMinutes());
      //var seconds=padDate(value.getSeconds());
      return year + "-" + month + "-" + day + " " + hour + ":" + minutes;
    }
  },

  methods: {
    async show_actionparams(tag) {
      this.showactionparams = true;
      this.globalhttpaction_id = tag.id;
      this.globalhttpaction_title = tag.title;

      const response = await this.axios
        .get(
          this.GLOBAL.baseURL +
            "/trigger/globalhttpaction/" +
            tag.id +
            "/httpkeyvalue/"
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      this.httpactparamList = response.data;
    },

    async addglobalhttpaction() {
      if (this.globalact_title && this.globalact_url) {
        var params = {
          title: this.globalact_title,
          url: this.globalact_url,
          owner: 1
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/trigger/globalhttpaction/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.globalhttpactionList.unshift(response.data);
      }
      else{
			this.$vs.notify({
				title:'提醒：',
				text:'动作名称、动作URL都不能为空.',
				color:'danger'
			})
		}

      this.globalact_title = "";
      this.globalact_url = "";
    },

    popupActiveHttpact_updatefunc(tag) {
      this.popupActiveHttpact_update = true;
      this.globalhttpaction_id_tmp = tag.id;
      this.globalhttpaction_title_tmp = tag.title;
      this.globalhttpaction_url_tmp = tag.url;
    },

    async globalhttpaction_update(globalhttpaction_id_tmp) {
      let params = new FormData();

      params.append("title", this.globalhttpaction_title_tmp); // 添加form表单中其他数据
      params.append("url", this.globalhttpaction_url_tmp);

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL +
            "/trigger/globalhttpaction/" +
            globalhttpaction_id_tmp +
            "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });

      this.globalhttpactionList.forEach(function(item, index, arr) {
        if (item.id == globalhttpaction_id_tmp) {
          arr.splice(index, 1, response.data);
        }
      });

      this.popupActiveHttpact_update = false;
      return true;
    },

    popupActiveHttpact_delfunc(tag) {
      this.popupActiveHttpact_del = true;
      this.globalhttpaction_id_tmp = tag.id;
    },

    async delglobalhttpact(globalhttpaction_id_tmp) {
      var url =
        this.GLOBAL.baseURL +
        "/trigger/globalhttpaction/" +
        globalhttpaction_id_tmp +
        "/";
      this.popupActiveHttpact_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.globalhttpactionList.forEach(function(item, index, arr) {
        if (item.id == globalhttpaction_id_tmp) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    async addhttpactparam(globalhttpaction_id) {
      if (this.httpactparamKey && this.httpactparamValue) {
        var params = {
          key: this.httpactparamKey,
          value: this.httpactparamValue,
          action: globalhttpaction_id
        };
        const response = await this.axios
          .post(
            this.GLOBAL.baseURL +
              "/trigger/globalhttpaction/" +
              globalhttpaction_id +
              "/httpkeyvalue/",
            params
          )
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.httpactparamList.unshift(response.data);
      }

      this.httpactparamKey = "";
      this.httpactparamValue = "";
    },

    popupActiveActparam_func(tr) {
      this.popupActiveActparam_del = true;
      this.httpactparam_id = tr.id;
    },

    async delactparam(httpactparam_id) {
      var url =
        this.GLOBAL.baseURL +
        "/trigger/globalhttpaction/" +
        this.globalhttpaction_id +
        "/httpkeyvalue/" +
        httpactparam_id +
        "/";
      this.popupActiveActparam_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.httpactparamList.forEach(function(item, index, arr) {
        if (item.id == httpactparam_id) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    //以下是MQTT方法
    async init_mqtt_action() {
      const response = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/globalmqttaction/")
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      console.log(response);
      this.globalmqttactionList = response.data.reverse();
    },

    async addglobalmqttaction() {
      if (this.global_mqtt_act_title && this.global_mqtt_topic) {
        var params = {
          title: this.global_mqtt_act_title,
          topic: this.global_mqtt_topic,
          owner: 1
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/trigger/globalmqttaction/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.globalmqttactionList.unshift(response.data);
      }

      else{
			this.$vs.notify({
				title:'提醒：',
				text:'MQTT动作名称、主题Topic都不能为空.',
				color:'danger'
			})
		}

      this.global_mqtt_act_title = "";
      this.global_mqtt_topic = "";
    },

    popupActiveMqttpact_delfunc(tag) {
      this.popupActiveMqttact_del = true;
      this.globalmqttaction_id_tmp = tag.id;
    },

    async delglobalmqttact(globalmqttaction_id_tmp) {
      var url =
        this.GLOBAL.baseURL +
        "/trigger/globalmqttaction/" +
        globalmqttaction_id_tmp +
        "/";
      this.popupActiveMqttact_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.globalmqttactionList.forEach(function(item, index, arr) {
        if (item.id == globalmqttaction_id_tmp) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    popupActiveMqttact_updatefunc(tag) {
      this.popupActiveMqttact_update = true;
      this.globalmqttaction_id_tmp = tag.id;
      this.globalmqttaction_title_tmp = tag.title;
      this.globalmqttaction_topic_tmp = tag.topic;
    },

    async globalmqttaction_update(globalmqttaction_id_tmp) {
      let params = new FormData();

      params.append("title", this.globalmqttaction_title_tmp); // 添加form表单中其他数据
      params.append("topic", this.globalmqttaction_topic_tmp);

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL +
            "/trigger/globalmqttaction/" +
            globalmqttaction_id_tmp +
            "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });

      this.globalmqttactionList.forEach(function(item, index, arr) {
        if (item.id == globalmqttaction_id_tmp) {
          arr.splice(index, 1, response.data);
        }
      });

      this.popupActiveMqttact_update = false;
      return true;
    },

    async show_mqttactionparams(tag) {
      this.showmqttactionparams = true;
      this.globalmqttaction_id = tag.id;
      this.globalmqttaction_title = tag.title;

      const response = await this.axios
        .get(
          this.GLOBAL.baseURL +
            "/trigger/globalmqttaction/" +
            tag.id +
            "/mqttkeyvalue/"
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      this.mqttactparamList = response.data;
    },

    async addmqttactparam(globalmqttaction_id) {
      if (this.mqttactparamKey && this.mqttactparamValue) {
        var params = {
          key: this.mqttactparamKey,
          value: this.mqttactparamValue,
          action: globalmqttaction_id
        };
        const response = await this.axios
          .post(
            this.GLOBAL.baseURL +
              "/trigger/globalmqttaction/" +
              globalmqttaction_id +
              "/mqttkeyvalue/",
            params
          )
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.mqttactparamList.unshift(response.data);
      }

      this.mqttactparamKey = "";
      this.mqttactparamValue = "";
    },

    popupActiveMqttActparam_func(tr) {
      this.popupActiveMqttActparam_del = true;
      this.mqttactparam_id = tr.id;
    },
    async delmqttactparam(mqttactparam_id) {
      var url =
        this.GLOBAL.baseURL +
        "/trigger/globalmqttaction/" +
        this.globalmqttaction_id +
        "/mqttkeyvalue/" +
        mqttactparam_id +
        "/";
      this.popupActiveMqttActparam_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.mqttactparamList.forEach(function(item, index, arr) {
        if (item.id == mqttactparam_id) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

  async  test_actionstatus(tag) {

      const response = await this.axios
          .get(this.GLOBAL.baseURL + "/trigger/globalhttpactions/"+tag.id+"/status")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
      alert(response.data.status)

   }

  },

  components: {
    "v-select": vSelect
  }
};
</script>

		