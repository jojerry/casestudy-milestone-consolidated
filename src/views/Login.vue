<template>
  <div class="container">
    <form>
      <div class="well">
        <h4>Login Page</h4>
        <p> {{message}} </p>

        <div class="form-group">
          <label class="pull-left"> Username </label>
         
          <input
            type="text"
            class="form-control"
            placeholder="Username"
            v-model="User.username"
            required
          />
        </div>
        <div class="form-group">
          <label class="pull-left"> Password </label>
          <input
            type="password"
            class="form-control"
            placeholder="Password "
            v-model="User.password"
            required
          />
        </div>
      </div>

      <button
        type="submit"
        class="btn btn-md btn-primary"
        @click="handleSubmit()"
      >
        Submit
      </button>
      <br />
      <br/>

      <router-link to="/register">
        <button
          type="submit"
          class="btn btn-md btn-primary"
        >
          Signup
        </button>
      </router-link>
    </form>
  </div>
</template>

<script>
/*eslint-disable */
import axios from "axios";
import router from '../router';
export default {
  // name: 'login',
  
  data() {
    return {
      User: { 
        // name: "",
        username: "",
        password: "",
        message: "",
      },
      submitted: false,
    };
  },
  methods: {
    handleSubmit() {
      this.submitted = true;
    
      // stop here if form is invalid
      let newUser = {
        // name: this.User.name,
        username: this.User.username,
        password: this.User.password,
        message: ""
      };
      console.log(newUser);
      axios
        // .post("http://127.0.0.1:5000/accounts/login", newUser)
        .post("https://z9ud8kb40m.execute-api.us-east-2.amazonaws.com/dev/login", newUser)

        .then((response) => {
          this.message = response;
          console.log(response);
          router.push({ name: 'Accountdetails' ,
          params:{username:newUser.username}
          })
        })
          
        
        .catch((error) => {
          console.log(error.response);
          this.message = "Invalid credentials"
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color:blue;
}
</style>