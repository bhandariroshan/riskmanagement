window.Event = new Vue();

Vue.component('mydivlabel', {
  props: ['riskfield'],
  template: `<div class="field">
                <label for="name" class="label">{{riskfield.risk_field_name}}</label>
                <div  v-if="riskfield.risk_field_data_type === 'Text'">
                    <div class="control">
                        <input class="input"
                            type="text"
                            v-bind:name="riskfield.risk_field_name"
                            v-bind:placeholder="riskfield.risk_field_name">
                    </div>
                </div>
                <div  v-if="riskfield.risk_field_data_type === 'Enum'">
                    <div class="control">
                        <input class="input"
                           v-bind:name="riskfield.risk_field_name"
                            v-bind:placeholder="riskfield.risk_field_name">
                    </div>
                </div>
                <div  v-if="riskfield.risk_field_data_type === 'Number'">
                    <div class="control">
                        <input class="input"
                            type="number"
                            name="points"
                            min="0"
                            max="100"
                            step="10"
                            value=""
                            v-bind:name="riskfield.risk_field_name"
                            v-bind:placeholder="riskfield.risk_field_name">
                    </div>
                </div>
                <div  v-if="riskfield.risk_field_data_type === 'Date'">
                    <div class="control">
                        <input class="input"
                            type="date"
                            v-bind:name="riskfield.risk_field_name"
                            v-bind:placeholder="riskfield.risk_field_name">
                    </div>
                </div>
              </div>`,
  methods:{}
})

var app7 = new Vue({
  el: '#app',
  data: {riskFieldList: []},
  mounted() {
    const vm = this;
    axios.get('/risks/types/1/')
      .then(function (response) {
        console.log(response);
        vm.riskFieldList = response.data.riskfields;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  created() {}
})
