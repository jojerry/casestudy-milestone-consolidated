<template>
  <div class="container">
    <form>
      <div class="well">
        <h4>Apply Loan</h4>
        <div class="form-group">
          <label class="pull-left"> Username </label>
          <input
            type="text"
            class="form-control"
            placeholder="Username"
            v-model="Loan.username"
            required
            minlength=6
          />
        </div>
        <div class="form-group">
          <label class="pull-left"> Loan Type</label>
          <input
            type="text"
            class="form-control"
            placeholder="Loan Type "
            v-model="Loan.loan_type"
            required
            minlength=3
          />
        </div>
        <div class="form-group">
          <label class="pull-left"> Loan Amount </label>
          <input
            type="number"
            class="form-control"
            placeholder="Loan amount"
            v-model="Loan.loan_Amount"
            required
            min=1000
          />
        <div class="form-group">
          <label class="pull-left"> Date  </label>
          <input
            type="text"
            class="form-control"
            placeholder="Date  "
            v-model="Loan.date"
            required
          />
        </div>
        <div class="form-group">
          <label class="pull-left"> Rate Of Interest</label>
          <input
            type="number"
            class="form-control"
            placeholder="Rate Of Interest"
            v-model="Loan.rate_of_interest"
            required
          />
        </div>
        <div class="form-group">
          <label class="pull-left"> Duration of loan</label>
          <input
            type="number"
            class="form-control"
            placeholder="Duration Of Loan"
            v-model="Loan.duration_of_loan"
            required
          />
        </div>
      </div>
        <button
          type="submit"
          class="btn btn-large btn-block btn-primary full-width"
          @click="addToAPI">
          Submit
        </button>
      <router-link to="/">
        <button class="btn btn-large btn-block btn-success full-width">
        Logout
      </button>
      </router-link>
      </div>
    </form>
  </div>
</template>

<script>
/*eslint-disable*/
import axios from 'axios'
import router from '../router';
export default {
  name: 'Loan',
  data () {
    return {
      username: this.$route.params.username,
      Loan: {
        username: '',
        loan_type: '',
        loan_Amount: '',
        date: '',
        rate_of_interest: '',
        duration_of_loan: ''
      }
    }
  },
  methods: {
    addToAPI () {
      let newLoan = {
        username: this.Loan.username,
        loan_type: this.Loan.loan_type,
        loan_Amount: this.Loan.loan_Amount,
        date: this.Loan.date,
        rate_of_interest: this.Loan.rate_of_interest,
        duration_of_loan: this.Loan.duration_of_loan
      }
      console.log(newLoan)
      axios
        // .post('http://127.0.0.1:5000/accounts/login/' + this.Loan.username + '/loans', newLoan)
        .post('https://7qq9a7hk76.execute-api.us-east-2.amazonaws.com/dev/'+ this.Loan.username, newLoan)
        
        .then((response) => {
          console.log(response)
          router.push({ name: 'ViewLoans' ,
          params:{username:this.Loan.username}
          })
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>