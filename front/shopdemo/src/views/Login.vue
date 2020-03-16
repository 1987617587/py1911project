<template>

	<div>
		<van-nav-bar title="登录" left-text="返回" left-arrow @click-left="onClickLeft" />
<!-- 		<label for="">用户名</label><input type="text" v-model="username">
		<br>
		<label for="">密码</label><input type="text" v-model="password">
		<br>
		<button @click="getToken()">请求Token</button> -->
		<!-- //引入vant表单 -->
		<!-- <br> -->
		<van-form @submit="getToken">
			<van-field v-model="username" name="用户名" label="用户名" placeholder="用户名" :rules="[{ required: true, message: '请填写用户名' }]" />
			<van-field v-model="password" type="password" name="密码" label="密码" placeholder="密码" :rules="[{ required: true, message: '请填写密码' }]" />
			<div style="margin: 16px;">
				<van-button round block type="info" native-type="submit">
					提交
				</van-button>
			</div>
		</van-form>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				username: "",
				password: "",

			}
		},
		created() {},
		methods: {
			onSubmit(values) {
				console.log('submit', values);
			},
			getToken() {
				this.$api.getToken({
					username: this.username,
					password: this.password
				}).then(res => {
					console.log("得到Token", res);
					this.$jsCookie.set("refresh", res.data.refresh)
					this.$jsCookie.set("access", res.data.access)
					this.$jsCookie.set("username", this.username)
					this.$store.commit("setlog",true)
					this.$router.push("/")
				}).catch(err => {
					console.log("发生错误", err);
					this.$toast("用户名或密码错误")
				})

			},
			onClickLeft() {
				this.$router.push("/")
			}
		}
	}
</script>

<style>
</style>
