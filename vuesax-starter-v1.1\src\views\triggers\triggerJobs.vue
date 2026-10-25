<template>
  <div class="mt-5">
    <div class="flex flex-wrap">
      <vs-tabs vs-alignment="fixed">
        <vs-tab vs-label="触发HTTP任务">
          <vs-row>
            <vs-col vs-type="flex" vs-justify="left" vs-align="center" vs-w="4">
              <vs-button
                color="success"
                type="filled"
                @click="popupActive_triggerjobcreate()"
              >新增触发HTTP任务</vs-button>
            </vs-col>

            <vs-popup title="创建一个新的触发任务" :active.sync="popupActive_triggerjob">
              <div class="vx-row">
                <div class="vx-col w-full">
                  <p>
                    任务名称
                    <font color="#FF0000">*</font>
                  </p>
                  <vs-input v-model="task_title_trigger" class="w-full" />
                  <br />
                </div>
                <div class="vx-col w-full">
                  <p>触发数据通道(只能填写上传数据通道ID)</p>
                  <vs-input v-model="trigger_datachannel" class="w-full" />
                  <br />
                </div>
                <div class="vx-col w-full">
                  <p>阈值-最大值-最小值</p>
                  <vs-input
                    v-model="trigger_threshold_value"
                    placeholder="阈值"
                    class="w-1/4 vs-col"
                  />
                  <vs-input v-model="trigger_maximum_value" placeholder="最大值" class="w-1/4 vs-col" />
                  <vs-input v-model="trigger_minimum_value" placeholder="最小值" class="w-1/4 vs-col" />
                </div>
                <div class="vx-col w-full">
                  <br />
                  <p>
                    选择触发条件
                    <font color="#FF0000">*</font>
                  </p>
                  <v-select
                    autocomplete
                    :options="['GREAT_THAN','EQUAL','GREAT_EQUAL','LITTLE_THAN','LITTLE_EQUAL','BETWEEN_MAX_MIN','NOT_BETWEEN_MAX_MIN']"
                    v-model="compare_choice"
                  ></v-select>
                  <br />
                </div>
              </div>
              <div class="vx-col w-full">
                <br />
                <p>任务运行状态</p>
                <ul class="centerx">
                  <li>
                    <vs-radio
                      class="vx-col w-1/4 mt-4"
                      color="success"
                      v-model="task_enabled_trigger"
                      vs-value="RUNNING"
                    >运行</vs-radio>
                    <vs-radio
                      class="vx-col w-1/4 mt-4"
                      color="danger"
                      v-model="task_enabled_trigger"
                      vs-value="PAUSING"
                    >暂停</vs-radio>
                  </li>
                </ul>
              </div>
              <div class="vx-col w-full">
                <br />
                <p>
                  选择执行动作
                  <font color="#FF0000">*</font>
                </p>
                <select
                  autocomplete
                  placeholder="选择执行动作"
                  class="selectExample w-full"
                  v-model="select1_action_trigger"
                  style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
                >
                  <option
                    :key="index"
                    :value="item.id"
                    v-for="(item,index) in options1_action_trigger"
                  >{{ item.title }}</option>
                </select>
              </div>

              <div class="vx-col w-full">
                <vs-button
                  class="vx-col w-1/3 mt-3"
                  type="border"
                  color="success"
                  v-on:click="addtriggerjob()"
                >添加触发任务</vs-button>
              </div>
            </vs-popup>

            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="8">
              <vs-input
                placeholder="搜索触发任务"
                v-model="knowledgeBaseSearchQuery_trigger"
                icon-pack="feather"
                icon="icon-search"
                class="w-full no-icon-border mt-4"
              />
            </vs-col>
          </vs-row>

          <vs-divider />

          <vs-table pagination max-items="10" :data="filteredKB" stripe>
            <template slot="thead">
              <vs-th>序号</vs-th>
              <vs-th>任务名称</vs-th>
              <vs-th>触发设备</vs-th>
              <vs-th>触发设备通道</vs-th>
              <vs-th>触发条件</vs-th>
              <vs-th>触发阈值</vs-th>
              <vs-th>最大值</vs-th>
              <vs-th>最小值</vs-th>
              <vs-th>被触发动作</vs-th>
              <vs-th>创建时间</vs-th>
              <vs-th>更新时间</vs-th>
              <vs-th>状态</vs-th>

              <vs-th style="padding-left:50px;">操作</vs-th>
            </template>

            <template slot-scope="{data}">
              <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                <vs-td :data="data[indextr].id">{{ data[indextr].id }}</vs-td>

                <vs-td :data="data[indextr].title">{{ data[indextr].title }}</vs-td>

                <vs-td :data="data[indextr].device">{{ data[indextr].device }}</vs-td>

                <vs-td :data="data[indextr].datachannel_title">{{ data[indextr].datachannel_title }}</vs-td>

                <vs-td
                  :data="data[indextr].compare_choice"
                  v-if="data[indextr].compare_choice=='GREAT_THAN'"
                >大于</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='EQUAL'"
                >等于</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='GREAT_EQUAL'"
                >大于等于</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='LITTLE_THAN'"
                >小于</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='LITTLE_EQUAL'"
                >小于等于</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='BETWEEN_MAX_MIN'"
                >最大、小值之间</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='NOT_BETWEEN_MAX_MIN'"
                >最大、小值之外</vs-td>
                <vs-td :data="data[indextr].threshold_value">{{ data[indextr].threshold_value }}</vs-td>

                <vs-td :data="data[indextr].maximum">{{ data[indextr].maximum }}</vs-td>

                <vs-td :data="data[indextr].minimum">{{ data[indextr].minimum }}</vs-td>

                <vs-td :data="data[indextr].action_title">{{ data[indextr].action_title }}</vs-td>

                <vs-td :data="data[indextr].created">{{ data[indextr].created | formatDate }}</vs-td>

                <vs-td :data="data[indextr].updated">{{ data[indextr].updated | formatDate }}</vs-td>

                <vs-td
                  :data="data[indextr].status_choice"
                  v-if="data[indextr].status_choice=='RUNNING'"
                  class="text-success"
                >运行</vs-td>
                <vs-td
                  :data="data[indextr].status_choice"
                  v-else-if="data[indextr].status_choice=='PAUSING'"
                  class="text-warning"
                >暂停</vs-td>

                <vs-td>
                  <vs-col
                    v-tooltip="'col - 4'"
                    vs-type="flex"
                    vs-w="1"
                    v-if="tr.status_choice=='PAUSING'"
                  >
                    <span class="text-danger">
                      <vx-tooltip color="success" text="启动任务">
                        <vs-button
                          radius
                          color="success"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-play"
                          @click="triggerjob_start(tr,indextr)"
                        ></vs-button>
                      </vx-tooltip>
                    </span>
                  </vs-col>
                  <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="1" v-else>
                    <span class="text-danger">
                      <vx-tooltip color="warning" text="停止任务">
                        <vs-button
                          radius
                          color="warning"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-pause"
                          @click="triggerjob_stop(tr,indextr)"
                        ></vs-button>
                      </vx-tooltip>
                    </span>
                  </vs-col>

                  <!-- 2022-12-21 ADD BEGIN -->
                  <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="1">
                    <span class="text-success">
                      <vx-tooltip color="success" text="编辑">
                        <vs-button
                          radius
                          color="success"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-edit-2"
                          @click="popupActiveTriggerJob_updatefunc(tr)"
                        ></vs-button>

                        <vs-popup
                          class="holamundo"
                          title="编辑触发任务"
                          :active.sync="popupActiveTriggerJob_update"
                          background-color="rgba(0,0,0,.1)"
                        >


                        <div class="vx-row">
                          <div class="vx-col w-full">
                            <p>
                              任务名称
                              <font color="#FF0000">*</font>
                            </p>
                            <vs-input v-model="task_title_trigger" class="w-full" />
                            <br />
                          </div>
                          <div class="vx-col w-full">
                            <p>触发数据通道(只能填写上传数据通道ID)</p>
                            <vs-input v-model="trigger_datachannel" class="w-full" />
                            <br />
                          </div>
                          <div class="vx-col w-full">
                            <p>阈值-最大值-最小值</p>
                            <vs-input
                              v-model="trigger_threshold_value"
                              placeholder="阈值"
                              class="w-1/4 vs-col"
                            />
                            <vs-input v-model="trigger_maximum_value" placeholder="最大值" class="w-1/4 vs-col" />
                            <vs-input v-model="trigger_minimum_value" placeholder="最小值" class="w-1/4 vs-col" />
                          </div>
                          <div class="vx-col w-full">
                            <br />
                            <p>
                              选择触发条件
                              <font color="#FF0000">*</font>
                            </p>
                            <v-select
                              autocomplete
                              :options="['GREAT_THAN','EQUAL','GREAT_EQUAL','LITTLE_THAN','LITTLE_EQUAL','BETWEEN_MAX_MIN','NOT_BETWEEN_MAX_MIN']"
                              v-model="compare_choice"
                            ></v-select>
                            <br />
                          </div>
                        </div>
                        <div class="vx-col w-full">
                          <br />
                          <p>任务运行状态</p>
                          <ul class="centerx">
                            <li>
                              <vs-radio
                                class="vx-col w-1/4 mt-4"
                                color="success"
                                v-model="task_enabled_trigger"
                                vs-value="RUNNING"
                              >运行</vs-radio>
                              <vs-radio
                                class="vx-col w-1/4 mt-4"
                                color="danger"
                                v-model="task_enabled_trigger"
                                vs-value="PAUSING"
                              >暂停</vs-radio>
                            </li>
                          </ul>
                        </div>
                        <div class="vx-col w-full">
                          <br />
                          <p>
                            选择执行动作
                            <font color="#FF0000">*</font>
                          </p>
                          <select
                            autocomplete
                            placeholder="选择执行动作"
                            class="selectExample w-full"
                            v-model="select1_action_trigger"
                            style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
                          >
                            <option
                              :key="index"
                              :value="item.id"
                              v-for="(item,index) in options1_action_trigger"
                            >{{ item.title }}</option>

                          </select>
                        </div>
                        <br>



                          <vs-row vs-justify="center">
                            <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                              <vs-button
                                color="success"
                                type="filled"
                                @click="update_triggerjob(triggerjob_id)"
                              >更新</vs-button>
                            </vs-col>

                            <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                              <vs-button
                                color="warning"
                                type="filled"
                                @click="popupActiveTriggerJob_update=false"
                              >取消</vs-button>
                            </vs-col>
                          </vs-row>
                        </vs-popup>
                      </vx-tooltip>
                    </span>
                  </vs-col>

                  <!-- 2022-12-21 ADD END -->

                  <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="1">
                    <span class="text-danger">
                      <vx-tooltip color="danger" text="删除">
                        <vs-button
                          radius
                          color="danger"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-trash"
                          @click="popupActiveTriggerJob_delfunc(tr)"
                        ></vs-button>

                        <vs-popup
                          class="holamundo"
                          title="删除触发任务"
                          :active.sync="popupActiveTriggerJob_del"
                          background-color="rgba(0,0,0,.1)"
                        >
                          <vs-row vs-justify="center">
                            <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                              <vs-button
                                color="danger"
                                type="filled"
                                @click="delete_triggerjob(triggerjob_id)"
                              >确认删除</vs-button>
                            </vs-col>

                            <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                              <vs-button
                                color="warning"
                                type="filled"
                                @click="popupActiveTriggerJob_del=false"
                              >取消</vs-button>
                            </vs-col>
                          </vs-row>
                        </vs-popup>
                      </vx-tooltip>
                    </span>
                  </vs-col>
                </vs-td>
              </vs-tr>
            </template>
          </vs-table>
        </vs-tab>
        <vs-tab vs-label="触发MQTT任务" @click="init_triggermqttlist()">
          <vs-row>
            <vs-col vs-type="flex" vs-justify="left" vs-align="center" vs-w="4">
              <vs-button
                color="success"
                type="filled"
                @click="popupActive_triggerjobcreate_mqtt()"
              >新增触发MQTT任务</vs-button>
            </vs-col>

            <vs-popup title="创建一个新的触发任务" :active.sync="popupActive_triggerjob_mqtt">
              <div class="vx-row">
                <div class="vx-col w-full">
                  <p>
                    任务名称
                    <font color="#FF0000">*</font>
                  </p>
                  <vs-input v-model="task_title_mqtt" class="w-full" />
                  <br />
                </div>
                <div class="vx-col w-full">
                  <p>触发数据通道(只能填写上传数据通道ID)</p>
                  <vs-input v-model="trigger_datachannel_mqtt" class="w-full" />
                  <br />
                </div>
                <div class="vx-col w-full">
                  <p>阈值-最大值-最小值</p>
                  <vs-input
                    v-model="trigger_threshold_value_mqtt"
                    placeholder="阈值"
                    class="w-1/4 vs-col"
                  />
                  <vs-input
                    v-model="trigger_maximum_value_mqtt"
                    placeholder="最大值"
                    class="w-1/4 vs-col"
                  />
                  <vs-input
                    v-model="trigger_minimum_value_mqtt"
                    placeholder="最小值"
                    class="w-1/4 vs-col"
                  />
                </div>
                <div class="vx-col w-full">
                  <br />
                  <p>
                    选择触发条件
                    <font color="#FF0000">*</font>
                  </p>
                  <v-select
                    autocomplete
                    :options="['GREAT_THAN','EQUAL','GREAT_EQUAL','LITTLE_THAN','LITTLE_EQUAL','BETWEEN_MAX_MIN','NOT_BETWEEN_MAX_MIN']"
                    v-model="compare_choice_mqtt"
                  ></v-select>
                  <br />
                </div>
              </div>
              <div class="vx-col w-full">
                <br />
                <p>任务运行状态</p>
                <ul class="centerx">
                  <li>
                    <vs-radio
                      class="vx-col w-1/4 mt-4"
                      color="success"
                      v-model="task_enabled_mqtt"
                      vs-value="RUNNING"
                    >运行</vs-radio>
                    <vs-radio
                      class="vx-col w-1/4 mt-4"
                      color="danger"
                      v-model="task_enabled_mqtt"
                      vs-value="PAUSING"
                    >暂停</vs-radio>
                  </li>
                </ul>
              </div>
              <div class="vx-col w-full">
                <br />
                <p>
                  选择执行动作
                  <font color="#FF0000">*</font>
                </p>
                <select
                  autocomplete
                  placeholder="选择执行动作"
                  class="selectExample w-full"
                  v-model="select1_action_mqtt"
                  style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
                >
                  <option
                    :key="index"
                    :value="item.id"
                    v-for="(item,index) in options1_action_mqtt"
                  >{{ item.title }}</option>
                </select>
              </div>

              <div class="vx-col w-full">
                <vs-button
                  class="vx-col w-1/3 mt-3"
                  type="border"
                  color="success"
                  v-on:click="addtriggerjob_mqtt()"
                >添加触发任务</vs-button>
              </div>
            </vs-popup>

            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="8">
              <vs-input
                placeholder="搜索触发MQTT任务"
                v-model="knowledgeBaseSearchQuery_mqtt"
                icon-pack="feather"
                icon="icon-search"
                class="w-full no-icon-border mt-4"
              />
            </vs-col>
          </vs-row>

          <vs-divider />

          <vs-table pagination max-items="10" :data="filteredKB_mqtt" stripe>
            <template slot="thead">
              <vs-th>序号</vs-th>
              <vs-th>任务名称</vs-th>
              <vs-th>触发设备</vs-th>
              <vs-th>触发设备通道</vs-th>
              <vs-th>触发条件</vs-th>
              <vs-th>触发阈值</vs-th>
              <vs-th>最大值</vs-th>
              <vs-th>最小值</vs-th>
              <vs-th>被触发动作</vs-th>
              <vs-th>创建时间</vs-th>
              <vs-th>更新时间</vs-th>
              <vs-th>状态</vs-th>

              <vs-th style="padding-left:50px;">操作</vs-th>
            </template>

            <template slot-scope="{data}">
              <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                <vs-td :data="data[indextr].id">{{ data[indextr].id }}</vs-td>

                <vs-td :data="data[indextr].title">{{ data[indextr].title }}</vs-td>

                <vs-td :data="data[indextr].device">{{ data[indextr].device }}</vs-td>

                <vs-td :data="data[indextr].datachannel_title">{{ data[indextr].datachannel_title }}</vs-td>

                <vs-td
                  :data="data[indextr].compare_choice"
                  v-if="data[indextr].compare_choice=='GREAT_THAN'"
                >大于</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='EQUAL'"
                >等于</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='GREAT_EQUAL'"
                >大于等于</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='LITTLE_THAN'"
                >小于</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='LITTLE_EQUAL'"
                >小于等于</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='BETWEEN_MAX_MIN'"
                >最大、小值之间</vs-td>
                <vs-td
                  :data="data[indextr].compare_choice"
                  v-else-if="data[indextr].compare_choice=='NOT_BETWEEN_MAX_MIN'"
                >最大、小值之外</vs-td>

                <vs-td :data="data[indextr].threshold_value">{{ data[indextr].threshold_value }}</vs-td>

                <vs-td :data="data[indextr].maximum">{{ data[indextr].maximum }}</vs-td>

                <vs-td :data="data[indextr].minimum">{{ data[indextr].minimum }}</vs-td>

                <vs-td :data="data[indextr].action_title">{{ data[indextr].action_title }}</vs-td>

                <vs-td :data="data[indextr].created">{{ data[indextr].created | formatDate }}</vs-td>

                <vs-td :data="data[indextr].updated">{{ data[indextr].updated | formatDate }}</vs-td>

                <vs-td
                  :data="data[indextr].status_choice"
                  v-if="data[indextr].status_choice=='RUNNING'"
                  class="text-success"
                >运行</vs-td>
                <vs-td
                  :data="data[indextr].status_choice"
                  v-else-if="data[indextr].status_choice=='PAUSING'"
                  class="text-warning"
                >暂停</vs-td>

                <vs-td>
                  <vs-col
                    v-tooltip="'col - 4'"
                    vs-type="flex"
                    vs-w="1"
                    v-if="tr.status_choice=='PAUSING'"
                  >
                    <span class="text-danger">
                      <vx-tooltip color="success" text="启动任务">
                        <vs-button
                          radius
                          color="success"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-play"
                          @click="triggerjob_start_mqtt(tr,indextr)"
                        ></vs-button>
                      </vx-tooltip>
                    </span>
                  </vs-col>
                  <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="1" v-else>
                    <span class="text-danger">
                      <vx-tooltip color="warning" text="停止任务">
                        <vs-button
                          radius
                          color="warning"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-pause"
                          @click="triggerjob_stop_mqtt(tr,indextr)"
                        ></vs-button>
                      </vx-tooltip>
                    </span>
                  </vs-col>

                  <!-- 2022-12-21 BEGIN -->
                  <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="1">
                    <span class="text-success">
                      <vx-tooltip color="success" text="编辑">
                        <vs-button
                          radius
                          color="success"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-edit-2"
                          @click="popupActiveTriggerJob_updatefunc_mqtt(tr)"
                        ></vs-button>

                        <vs-popup
                          class="holamundo"
                          title="编辑触发任务"
                          :active.sync="popupActiveTriggerJob_update_mqtt"
                          background-color="rgba(0,0,0,.1)"
                        >

                        <div class="vx-row">
                          <div class="vx-col w-full">
                            <p>
                              任务名称
                              <font color="#FF0000">*</font>
                            </p>
                            <vs-input v-model="task_title_mqtt" class="w-full" />
                            <br />
                          </div>
                          <div class="vx-col w-full">
                            <p>触发数据通道(只能填写上传数据通道ID)</p>
                            <vs-input v-model="trigger_datachannel_mqtt" class="w-full" />
                            <br />
                          </div>
                          <div class="vx-col w-full">
                            <p>阈值-最大值-最小值</p>
                            <vs-input
                              v-model="trigger_threshold_value_mqtt"
                              placeholder="阈值"
                              class="w-1/4 vs-col"
                            />
                            <vs-input
                              v-model="trigger_maximum_value_mqtt"
                              placeholder="最大值"
                              class="w-1/4 vs-col"
                            />
                            <vs-input
                              v-model="trigger_minimum_value_mqtt"
                              placeholder="最小值"
                              class="w-1/4 vs-col"
                            />
                          </div>
                          <div class="vx-col w-full">
                            <br />
                            <p>
                              选择触发条件
                              <font color="#FF0000">*</font>
                            </p>
                            <v-select
                              autocomplete
                              :options="['GREAT_THAN','EQUAL','GREAT_EQUAL','LITTLE_THAN','LITTLE_EQUAL','BETWEEN_MAX_MIN','NOT_BETWEEN_MAX_MIN']"
                              v-model="compare_choice_mqtt"
                            ></v-select>
                            <br />
                          </div>
                        </div>
                        <div class="vx-col w-full">
                          <br />
                          <p>任务运行状态</p>
                          <ul class="centerx">
                            <li>
                              <vs-radio
                                class="vx-col w-1/4 mt-4"
                                color="success"
                                v-model="task_enabled_mqtt"
                                vs-value="RUNNING"
                              >运行</vs-radio>
                              <vs-radio
                                class="vx-col w-1/4 mt-4"
                                color="danger"
                                v-model="task_enabled_mqtt"
                                vs-value="PAUSING"
                              >暂停</vs-radio>
                            </li>
                          </ul>
                        </div>
                        <div class="vx-col w-full">
                          <br />
                          <p>
                            选择执行动作
                            <font color="#FF0000">*</font>
                          </p>
                          <select
                            autocomplete
                            placeholder="选择执行动作"
                            class="selectExample w-full"
                            v-model="select1_action_mqtt"
                            style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
                          >
                            <option
                              :key="index"
                              :value="item.id"
                              v-for="(item,index) in options1_action_mqtt"
                            >{{ item.title }}</option>
                          </select>
                        </div>

                        <br>
                          <vs-row vs-justify="center">
                            <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                              <vs-button
                                color="success"
                                type="filled"
                                @click="update_triggerjob_mqtt(triggerjob_id_mqtt)"
                              >更新</vs-button>
                            </vs-col>

                            <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                              <vs-button
                                color="warning"
                                type="filled"
                                @click="popupActiveTriggerJob_update_mqtt=false"
                              >取消</vs-button>
                            </vs-col>
                          </vs-row>
                        </vs-popup>
                      </vx-tooltip>
                    </span>
                  </vs-col>

                  <!-- 2022-12-21 END -->

                  <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="1">
                    <span class="text-danger">
                      <vx-tooltip color="danger" text="删除">
                        <vs-button
                          radius
                          color="danger"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-trash"
                          @click="popupActiveTriggerJob_delfunc_mqtt(tr)"
                        ></vs-button>

                        <vs-popup
                          class="holamundo"
                          title="删除触发任务"
                          :active.sync="popupActiveTriggerJob_del_mqtt"
                          background-color="rgba(0,0,0,.1)"
                        >
                          <vs-row vs-justify="center">
                            <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                              <vs-button
                                color="danger"
                                type="filled"
                                @click="delete_triggerjob_mqtt(triggerjob_id_mqtt)"
                              >确认删除</vs-button>
                            </vs-col>

                            <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                              <vs-button
                                color="warning"
                                type="filled"
                                @click="popupActiveTriggerJob_del_mqtt=false"
                              >取消</vs-button>
                            </vs-col>
                          </vs-row>
                        </vs-popup>
                      </vx-tooltip>
                    </span>
                  </vs-col>
                </vs-td>
              </vs-tr>
            </template>
          </vs-table>
        </vs-tab>
      </vs-tabs>
    </div>
  </div>
</template>

<script>
var padDate = function(va) {
  va = va < 10 ? "0" + va : va;
  return va;
};

import { FormWizard, TabContent } from "vue-form-wizard";
import "vue-form-wizard/dist/vue-form-wizard.min.css";
import vSelect from "vue-select";

import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import "flatpickr/dist/flatpickr.min.css";

export default {
  data() {
    return {
      triggerjobsList: [],
      url: this.GLOBAL.baseURL,
      knowledgeBaseSearchQuery_trigger: "",
      popupActive_triggerjob: false,
      task_title_trigger: "",//g
      trigger_datachannel: "",
      trigger_threshold_value: "",
      trigger_maximum_value: "100",
      trigger_minimum_value: "1",
      compare_choice: "GREAT_THAN",

      task_enabled_trigger: true,//g

      select1_action_trigger: 0,//g
      options1_action_trigger: [],//g

      popupActiveTriggerJob_del: false,
      triggerjob_id: "",
      // 以下是mqtt动作任务
      popupActive_triggerjob_mqtt: false,
      select1_action_mqtt: 0,
      options1_action_mqtt: [],
      triggerjobsList_mqtt: [],
      knowledgeBaseSearchQuery_mqtt: "",
      task_title_mqtt: "",
      trigger_datachannel_mqtt: "",
      trigger_threshold_value_mqtt: "",
      trigger_maximum_value_mqtt: "100",
      trigger_minimum_value_mqtt: "1",
      compare_choice_mqtt: "GREAT_THAN",
      task_enabled_mqtt: true,

      popupActiveTriggerJob_del_mqtt: false,
      triggerjob_id_mqtt: "",
      // 2022-12-21
      popupActiveTriggerJob_update: false,
      popupActiveTriggerJob_update_mqtt: false,
    };
  },
  computed: {
    filteredKB() {
      return this.triggerjobsList.filter(
        item =>
          item.title
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_trigger.toLowerCase()) ||
          item.datachannel_title
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_trigger.toLowerCase()) ||
          item.device
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_trigger.toLowerCase())
      );
    },
    filteredKB_mqtt() {
      return this.triggerjobsList_mqtt.filter(
        item =>
          item.title
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_mqtt.toLowerCase()) ||
          item.datachannel_title
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_mqtt.toLowerCase()) ||
          item.device
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_mqtt.toLowerCase())
      );
    }
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

  created: async function() {
    const response = await this.axios
      .get(this.GLOBAL.baseURL + "/trigger/triggerhttpjobs/")
      .catch(function(error) {
        console.log(error);
        return error.response.data;
      });
    this.triggerjobsList = response.data;
  },

  methods: {
    // async showscheduleinput() {
    //   if (this.schedule_type == "INTERVAL") {
    //     this.schedule_interval_input = true;
    //     this.schedule_cron_input = false;
    //     this.schedule_clocked_input = false;
    //   }
    //   if (this.schedule_type == "CRONS") {
    //     this.schedule_interval_input = false;
    //     this.schedule_cron_input = true;
    //     this.schedule_clocked_input = false;
    //   }
    //   if (this.schedule_type == "CLOCKED") {
    //     this.schedule_interval_input = false;
    //     this.schedule_cron_input = false;
    //     this.schedule_clocked_input = true;
    //   }
    // },

    async popupActive_triggerjobcreate() {
      this.popupActive_triggerjob = true;
      const response2 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/globalhttpaction/")
        .catch(function(error) {
          console.log(error);
          return error.response2.data;
        });
      console.log(response2);
      this.options1_action_trigger = response2.data;
    },

    async addtriggerjob() {
      if (
        this.task_title_trigger &&
        this.select1_action_trigger &&
        this.trigger_datachannel &&
        this.trigger_threshold_value
      ) {
        var params = {
          title: this.task_title_trigger,
          datachannel: this.trigger_datachannel,
          threshold_value: this.trigger_threshold_value,
          maximum: this.trigger_maximum_value,
          minimum: this.trigger_minimum_value,
          action: this.select1_action_trigger,
          status_choice: this.task_enabled_trigger,
          compare_choice: this.compare_choice,
          owner: 1
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/trigger/triggerhttpjobs/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);

        const response2 = await this.axios
          .get(this.GLOBAL.baseURL + "/trigger/triggerhttpjobs/")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
        this.triggerjobsList = response2.data;

        this.popupActive_triggerjob = false;
        return true;
      }
      else{
           this.$vs.notify({
            title:'提醒：',
            text:'任务名称、数据通道、触发动作都不能为空.',
            color:'danger'
          })
         }
    },

    popupActiveTriggerJob_delfunc(tr) {
      this.popupActiveTriggerJob_del = true;
      this.triggerjob_id = tr.id;
    },
    // 2022-12-21 BEGIN
    async popupActiveTriggerJob_updatefunc(tr) {
      this.popupActiveTriggerJob_update = true;
      this.triggerjob_id = tr.id;
      this.task_title_trigger = tr.title;
      this.trigger_datachannel = tr.datachannel;
      this.trigger_threshold_value = tr.threshold_value;
      this.compare_choice = tr.compare_choice;
      this.task_enabled_trigger = tr.status_choice;
      this.select1_action_trigger = tr.action;

      const response2 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/globalhttpaction/")
        .catch(function(error) {
          console.log(error);
          return error.response2.data;
        });
      console.log(response2);
      this.options1_action_trigger = response2.data;
    },


    async update_triggerjob(triggerjob_id) {
      if (
        this.task_title_trigger &&
        this.select1_action_trigger &&
        this.trigger_datachannel &&
        this.trigger_threshold_value
      ) {
        var params = {
          title: this.task_title_trigger,
          datachannel: this.trigger_datachannel,
          threshold_value: this.trigger_threshold_value,
          maximum: this.trigger_maximum_value,
          minimum: this.trigger_minimum_value,
          action: this.select1_action_trigger,
          status_choice: this.task_enabled_trigger,
          compare_choice: this.compare_choice,
        };
        const response = await this.axios
          .patch(this.GLOBAL.baseURL + "/trigger/triggerhttpjobs/"+triggerjob_id+"/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
          console.log(response.data);
        this.popupActiveTriggerJob_update = false;

        const response2 = await this.axios
          .get(this.GLOBAL.baseURL + "/trigger/triggerhttpjobs/")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
        this.triggerjobsList = response2.data;

        return true;
      }
      else{
           this.$vs.notify({
            title:'提醒：',
            text:'任务名称、数据通道、触发动作都不能为空.',
            color:'danger'
          })
         }

    },

    // 2022-12-21 END

    async delete_triggerjob(triggerjob_id) {
      var url =
        this.GLOBAL.baseURL + "/trigger/triggerhttpjobs/" + triggerjob_id + "/";
      this.popupActiveTriggerJob_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.triggerjobsList.forEach(function(item, index, arr) {
        if (item.id == triggerjob_id) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    async triggerjob_start(tr, indextr) {
      var params = { status_choice: "RUNNING" };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/trigger/triggerhttpjobs/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.triggerjobsList[indextr].status_choice = "RUNNING";
      }
    },

    async triggerjob_stop(tr, indextr) {
      var params = { status_choice: "PAUSING" };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/trigger/triggerhttpjobs/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.triggerjobsList[indextr].status_choice = "PAUSING";
      }
    },

    //以下是MQTT动作任务
    async popupActive_triggerjobcreate_mqtt() {
      this.popupActive_triggerjob_mqtt = true;
      const response2 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/globalmqttaction/")
        .catch(function(error) {
          console.log(error);
          return error.response2.data;
        });
      console.log(response2);
      this.options1_action_mqtt = response2.data;
    },
    async init_triggermqttlist() {
      const response = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/triggermqttjobs/")
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      this.triggerjobsList_mqtt = response.data;
    },

    async addtriggerjob_mqtt() {
      if (
        this.task_title_mqtt &&
        this.select1_action_mqtt &&
        this.trigger_datachannel_mqtt &&
        this.trigger_threshold_value_mqtt
      ) {
        var params = {
          title: this.task_title_mqtt,
          datachannel: this.trigger_datachannel_mqtt,
          threshold_value: this.trigger_threshold_value_mqtt,
          maximum: this.trigger_maximum_value_mqtt,
          minimum: this.trigger_minimum_value_mqtt,
          action: this.select1_action_mqtt,
          status_choice: this.task_enabled_mqtt,
          compare_choice: this.compare_choice_mqtt,
          owner: 1
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/trigger/triggermqttjobs/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);

        const response2 = await this.axios
          .get(this.GLOBAL.baseURL + "/trigger/triggermqttjobs/")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
        this.triggerjobsList_mqtt = response2.data;

        this.popupActive_triggerjob_mqtt = false;
        return true;
      }
      else{
           this.$vs.notify({
            title:'提醒：',
            text:'任务名称、数据通道、触发动作都不能为空.',
            color:'danger'
          })
         }
    },
    popupActiveTriggerJob_delfunc_mqtt(tr) {
      this.popupActiveTriggerJob_del_mqtt = true;
      this.triggerjob_id_mqtt = tr.id;
    },

    // 2022-12-21 BEGIN

    async popupActiveTriggerJob_updatefunc_mqtt(tr) {
      this.popupActiveTriggerJob_update_mqtt = true;
      this.triggerjob_id_mqtt = tr.id;
      this.task_title_mqtt = tr.title;
      this.trigger_datachannel_mqtt = tr.datachannel;
      this.trigger_threshold_value_mqtt = tr.threshold_value;
      this.trigger_maximum_value_mqtt = tr.maximum;
      this.trigger_minimum_value_mqtt = tr.minimum;
      this.compare_choice_mqtt = tr.compare_choice;
      this.task_enabled_mqtt = tr.status_choice;
      this.select1_action_mqtt = tr.action;

      const response2 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/globalmqttaction/")
        .catch(function(error) {
          console.log(error);
          return error.response2.data;
        });
      this.options1_action_mqtt = response2.data;
    },

    async update_triggerjob_mqtt(triggerjob_id_mqtt) {

       if (
        this.task_title_mqtt &&
        this.select1_action_mqtt &&
        this.trigger_datachannel_mqtt &&
        this.trigger_threshold_value_mqtt
      ) {
        var params = {
          title: this.task_title_mqtt,
          datachannel: this.trigger_datachannel_mqtt,
          threshold_value: this.trigger_threshold_value_mqtt,
          maximum: this.trigger_maximum_value_mqtt,
          minimum: this.trigger_minimum_value_mqtt,
          action: this.select1_action_mqtt,
          status_choice: this.task_enabled_mqtt,
          compare_choice: this.compare_choice_mqtt,
        };
        const response = await this.axios
          .patch(this.GLOBAL.baseURL + "/trigger/triggermqttjobs/"+triggerjob_id_mqtt+"/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.popupActiveTriggerJob_update_mqtt = false;

        const response2 = await this.axios
          .get(this.GLOBAL.baseURL + "/trigger/triggermqttjobs/")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
        this.triggerjobsList_mqtt = response2.data;
        return true;
      }
      else{
           this.$vs.notify({
            title:'提醒：',
            text:'任务名称、数据通道、触发动作都不能为空.',
            color:'danger'
          })
         }

    },

    

    // 2022-12-21 END
    async delete_triggerjob_mqtt(triggerjob_id_mqtt) {
      var url =
        this.GLOBAL.baseURL +
        "/trigger/triggermqttjobs/" +
        triggerjob_id_mqtt +
        "/";
      this.popupActiveTriggerJob_del_mqtt = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.triggerjobsList_mqtt.forEach(function(item, index, arr) {
        if (item.id == triggerjob_id_mqtt) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    async triggerjob_start_mqtt(tr, indextr) {
      var params = { status_choice: "RUNNING" };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/trigger/triggermqttjobs/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.triggerjobsList_mqtt[indextr].status_choice = "RUNNING";
      }
    },

    async triggerjob_stop_mqtt(tr, indextr) {
      var params = { status_choice: "PAUSING" };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/trigger/triggermqttjobs/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.triggerjobsList_mqtt[indextr].status_choice = "PAUSING";
      }
    }
  },

  components: {
    "v-select": vSelect,
    FormWizard,
    TabContent,
    flatPickr
  }
};
</script>