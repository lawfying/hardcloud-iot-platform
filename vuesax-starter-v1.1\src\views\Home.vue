<!-- =========================================================================================
	File Name: PopupInnerPopup.vue
	Description: create inner popup
	----------------------------------------------------------------------------------------
	Item Name: Vuesax Admin - VueJS Dashboard Admin Template
	Version: 1.1
	Author: Pixinvent
	Author URL: hhttp://www.themeforest.net/user/pixinvent
========================================================================================== -->


<template>

	<vx-card title="Inner Popup" code-toggler>

		<p>You can add one popup inside another</p>

		<baidu-map class="map" ak='2140eb7ba44386b17ef7f6601239b6b9' :center="center" :zoom="zoom" @ready="handler" style="width:100%;height:500px;"></baidu-map>
		
		<div class="demo-alignment">

			<vs-button @click="popupActive2=true" color="primary" type="filled">Open Popup</vs-button>

			<vs-popup classContent="popup-example" title="Lorem ipsum dolor sit amet" :active.sync="popupActive2" style="z-index:1;">
				<vs-input class="inputx mb-3" placeholder="Placeholder" v-model="value1" />
				<vs-input disabled class="inputx mb-3" placeholder="Disabled" v-model="value2" />
				<vs-button @click="popupActive3=true" color="primary" type="filled">Open Inner Popup</vs-button>

					<div class="demo-alignment">
			<vs-select autocomplete class="selectExample" v-model="select1" style="z-index:10;">
				<vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in options1" />
			</vs-select>
			<vs-select autocomplete class="selectExample" v-model="select2">
				<vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in options2" />
			</vs-select>
			<vs-select autocomplete disabled="true" class="selectExample" v-model="select3">
				<vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in options3" />
			</vs-select>
		</div>

				<vs-popup title="Inner popup" :active.sync="popupActive3">
					<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
				</vs-popup>
			</vs-popup>
					
	

		</div>
<p>ddddddddddddddddd</p>

                  <VuePerfectScrollbar  :settings="settings" style="height:500px;">

					<ul class="activity-timeline" >

						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
						<li>
							<div class="timeline-icon bg-success">
								<feather-icon icon="CheckIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
							</div>
							<div class="timeline-info">
								<span class="activity-desc">Candy ice cream cake. Halvah gummi bears</span>
							</div>
							<small class="text-grey activity-e-time">20 mins ago</small>
						</li>
					</ul>

</VuePerfectScrollbar>
	



	</vx-card>
</template>

<script>

import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
import VuePerfectScrollbar from 'vue-perfect-scrollbar'


export default {
	data() {
		return {
settings: {
				maxScrollbarLength: 60,
				wheelSpeed: 0.30,
			},
			
      center: {lng: 0, lat: 0},
      zoom: 3,
			value1: '',
			value2: '',
			popupActive2: false,
			popupActive3: false,
			select1: 3,
			select2: 7,
			select3: 2,
			options1: [
				{ text: 'IT', value: 0 },
				{ text: 'Blade Runner', value: 2 },
				{ text: 'Thor Ragnarok', value: 3 },
			],
			options2: [
				{ text: 'Square', value: 1 },
				{ text: 'Rectangle', value: 2 },
				{ text: 'Rombo', value: 3 },
				{ text: 'Romboid', value: 4 },
				{ text: 'Trapeze', value: 5 },
				{ text: 'Triangle', value: 6 },
				{ text: 'Polygon', value: 7 },
				{ text: 'Regular polygon', value: 8 },
				{ text: 'Circumference', value: 9 },
				{ text: 'Circle', value: 10 },
				{ text: 'Circular sector', value: 11 },
				{ text: 'Circular trapeze', value: 12 },
			],
			options3: [
				{ text: 'Red', value: 1 },
				{ text: 'Green', value: 2 },
				{ text: 'Blue', value: 3 },
				{ text: 'Purple', value: 4 },
			],
		}
	},
	methods:{
		handler ({BMap, map}) {
				console.log(BMap, map)
				this.center.lng = 116.404
				this.center.lat = 39.915
				this.zoom = 15
				},
	},
	components: {
		BaiduMap,
		VuePerfectScrollbar 
  }

	
}
</script>
