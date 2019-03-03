<template>
  <div class="header-home">
    <div class="header-left">
      <div class="iconfont back-icon">&#xe60f;</div>
    </div>
    <div class="header-input" >
      <span class="iconfont">&#xe61b;</span>
      输入游玩\乐园\主题
    </div>
    <div class="header-right">
      {{this.city}}
      <span class="iconfont">&#xe652;</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  props: {
    city: String
  },

}
</script>

<style lang="stylus" scoped>
  @import '~styles/varibles.styl'
  .header-home
    display: flex
    background : $bgColor
    line-height: .86rem
    .header-left
      width: .64rem
      float: left
      .back-icon
        text-align: center
    .header-right
      width: 1.24rem
      float: right
      text-align: center
    .header-input
      padding-left: .2rem
      margin-left: .2rem
      flex:1
      background: #fff
      margin-top: .12rem
      border-radius: .1rem
      height: .62rem
      line-height : .62rem
      corlor: #ccc

</style>
