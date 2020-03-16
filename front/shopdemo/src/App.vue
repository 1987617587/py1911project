<template>
	<div id="app">
		<div id="nav">
			<router-link to="/">首页</router-link> |
			<!-- <router-link to="/about">关于</router-link>| -->
			<span v-if="!islog">
				
				<router-link to="/register">注册</router-link>|
				<router-link to="/login">登录</router-link>|
			</span>


			<span v-else>
				<router-link to="/usercenter">用户：{{ $jsCookie.get('username') }}</router-link>|
				<!-- <router-link to="/login">退出</router-link> -->
				<span @click="logout">退出</span>
			</span>

		</div>
		<router-view />
	</div>
</template>
<script>
	export default {
		data() {
			return {

				

			}
		},
		computed:{
			// 计算属性不能判断cookie变化 但是可以判断 store数据状态管理器数据变化
			islog(){
				return this.$store.getters.getlog
			}
		},
		created() {
			// islog:this.$store.state.islog,
		},
		methods: {
			
			logout(){
				console.log("退出")
				this.$jsCookie.remove("username")
				this.$jsCookie.remove("access")
				this.$jsCookie.remove("refresh")
				this.$jsCookie.remove("userinfo")
				this.$store.commit("setlog",false)
				this.$router.push("/login")
			}
		},
	}
</script>

<style lang="less">
	#app {
		font-family: Avenir, Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
	}

	#nav {
		padding: 30px;

		a {
			font-weight: bold;
			color: #2c3e50;

			&.router-link-exact-active {
				color: #42b983;
			}
		}
	}
</style>
