<template>

	<div>
		<van-nav-bar title="注册" left-text="返回" left-arrow @click-left="onClickLeft" />
		<!-- 		<label for="">用户名</label><input type="text" v-model="username">
		<br>
		<label for="">密码</label><input type="text" v-model="password">
		<br>
		<button @click="getToken()">请求Token</button> -->
		<!-- //引入vant表单 -->
		<!-- <br> -->
		<van-form @submit="createuser">
			<van-field v-model="username" name="用户名" label="用户名" placeholder="用户名" :rules="[{ required: true, message: '请填写用户名' }]" />
			<van-field v-model="email" name="邮箱" label="邮箱" placeholder="邮箱" :rules="[{ required: false, message: '请填写邮箱' }]" />
			<van-field v-model="tel" name="手机号" label="手机号" placeholder="手机号" :rules="[{ required: false, message: '请填写手机号' }]" />
			<van-field v-model="password" type="password" name="密码" label="密码" placeholder="密码" :rules="[{ required: true, message: '请填写密码' }]" />
			<van-field v-model="repassword" type="password" name="重复密码" label="重复密码" placeholder="重复密码" :rules="[{ required: true, message: '请重复填写密码' }]" />
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
				email: "",
				tel: "",
				password: "",
				repassword: "",


			}
		},
		created() {},
		methods: {
			onSubmit(values) {
				console.log('submit', values);
			},
			createuser() {
				console.log("注册信息")
				if (this.password == this.repassword) {
					this.$api.register({
						username: this.username,
						email: this.email,
						tel:this.tel,
						password:this.password,
						password2:this.repassword,
						
						
					}).then(res => {
						console.log("注册成功", res);
						this.$router.push('/login')
					}).catch(err => {
						console.log("发生错误", err);
					})
				}
				else{
					this.$toast("密码不一致")
				}
			},
			onClickLeft() {
				this.$router.push("/")
			}
		}
	}
</script>

<style>
</style>
