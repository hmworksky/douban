<template>
  <div>
    <city-header></city-header>
    <city-search></city-search>
    <city-list :city="cities" :hot="hotCities"></city-list>
    <city-alphabet :city="cities"></city-alphabet>
  </div>
</template>

<script>
import axios from 'axios'
import CityHeader from './components/Header'
import CitySearch from './components/Search'
import CityList from './components/List'
import CityAlphabet from './components/Alphabet'
export default {
  name: 'City',
  components: {
    CityHeader,
    CitySearch,
    CityList,
    CityAlphabet
  },
  data () {
    return {
      cities: {},
      hotCities: []
    }
  },
  methods: {
    getCityInfo () {
      axios.get('/api/city.json')
        .then(this.handleCitySuccess)
    },
    handleCitySuccess (res) {
      res = res.data
      if (res.data && res.ret) {
        const data = res.data
        this.cities = data.cities
        this.hotCities = data.hotCities
      }
    }
  },
  mounted () {
    this.getCityInfo();
  }
}
</script>

<style lang="stylus" scoped>

</style>
