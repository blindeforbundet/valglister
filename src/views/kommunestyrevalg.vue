<template>
  <div class="home">
  <h1>ValglKomuneister</h1>

  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import json from '@/valglister/komunestyrevalg.json'
export default {
  name: 'home',
  components: {
    HelloWorld
  },
  created() {
    json.forEach((v)=>{
      this.partier[v.partinavn] = v.partikode
    })

    var fylker_dict = {}
    json.forEach((v)=>{
      fylker_dict[v.fylke] = true
      console.log(v)
    })
    this.fylker = [ ...Object.keys(fylker_dict)]
    this.fylker = this.fylker.sort()
  },
  data(){
    return{
        myJson: json,
        partier: {},
        selected_parti: undefined,
        selected_fylke: undefined,
        fylker: undefined
    }
  },
  computed: {
      filtered_parti() {
        var filtered_data = this.myJson
        if(this.selected_fylke !== undefined) {
          filtered_data = filtered_data.filter(i => i.fylke == this.selected_fylke)
        }
        if(this.selected_parti !== undefined){
          filtered_data = filtered_data.filter(i => i.partikode == this.selected_parti)

        }
        return filtered_data
    },

  }
}
</script>
