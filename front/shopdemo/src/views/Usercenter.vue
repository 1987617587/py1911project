<template>
	<div class="usercenter">
		<h2>用户中心</h2>
		<!-- <div v-if="userinfo">
			用户名：{{userinfo.username}}
			<br>
			邮箱：{{userinfo.email}}
			<br>
			手机号：{{userinfo.tel}}
			<br>
			注册时间：{{userinfo.date_joined|dataFormat}}
		</div> -->
		<div v-if="userinfo" class="updateinfo">
			<h2>修改信息</h2>
			<van-form @submit="updateinfo">
				<van-field v-model="userinfo.username" name="用户名" label="用户名" placeholder="用户名" :rules="[{ required: false, message: '请填写新的用户名' }]" />
				<van-field v-model="userinfo.tel" name="手机号" label="手机号" placeholder="手机号" :rules="[{ required: false, message: '请填写新的手机号' }]" />
				<van-field v-model="userinfo.email" name="email" label="邮箱" placeholder="邮箱" :rules="[{ required: false, message: '请填写新的邮箱' }]" />
				<van-field v-model="userinfo.password" type="password" name="password" label="密码" placeholder="密码" :rules="[{ required: false, message: '请填写新的密码' }]" />
				<div style="margin: 16px;">
					<van-button round block type="info" native-type="submit">
						提交
					</van-button>
				</div>
			</van-form>
		</div>
		<div v-else>
			<h2>未找到信息</h2>
		</div>
		
	</div>

</template>

<script>
	export default {
		data() {
			return {
				userinfo: null,

			}
		},
		computed: {
				
		},
		created() {
			this.$api.getUserinfo().then(res => {
				console.log("个人信息", res)
				this.userinfo = res.data;
				this.$jsCookie.set("userinfo", res.data)

			}).catch(err => {
				console.log("出粗了")
			})
		},
		methods: {
			updateinfo() {
				this.$api.updateUserinfo({
					userinfo:this.userinfo
				}).then(res => {
					// this.$store.commit("setlog",true)
					console.log("修改个人信息成功", res)
					this.$router.go(0)
				}).catch(err => {
					console.log("出粗了")
				})
			}


		},
		filters: {
			dataFormat(date) {
				date = new Date(date)
				console.log(date, typeof(date));
				return `${date.getFullYear()}--${date.getMonth()+1}--${date.getDate()}`
			}
		}
	}
</script>

<style>
</style>
