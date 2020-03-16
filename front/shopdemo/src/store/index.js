import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
	  islog:false
  },
  getters:{
  	  getlog(state){
  		  return state.islog
  	  }
  },
  mutations: {
	  setlog(status,b){
		  status.islog=b
		  
	  }
  },
  actions: {
  },
  modules: {
  }
})
