window.Event = new Vue();


Vue.component('mydivlabel', {
  props: ['riskfield'],
  template: `<div class="field" style="margin: 6px;">
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
                            <select v-bind:name="riskfield.risk_field_name"  class="input">
                              <option disabled value="" selected="selected">Please select one</option>
                              <option v-for="eachchoice in riskfield.risk_field_choices" v-bind:value="eachchoice.choice">
                              {{eachchoice.choice}}
                              </option>
                            </select>
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


var app1 = new Vue({
  el: '#app1',
  delimiters: ['${', '}'],
  data: {
        riskTypes: [],
        selected: 'Please select one'
  },
  methods: {
    loadnewForm: function(e){
           var selected_id = e.target.value;
           window.location = '/show/' + selected_id + '/'
        }
  },
  mounted() {
    const vm = this;
    axios.get('/risks/types/')
      .then(function (response) {
        vm.riskTypes = response.data;
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  created() {}
})

var app7 = new Vue({
  el: '#app',
  data: {
        riskFieldList: [],
        selected: 'Please select one'
  },
  mounted() {
    const vm = this;
    axios.get('/risks/types/' + risktypeid + '/')
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
