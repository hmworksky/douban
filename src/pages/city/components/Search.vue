<template>
    <div class="search">
      <input class="search-input" type="text" placeholder="请输入城市名或拼音" />
    </div>
</template>

<script>
export default {
  name: 'CitySearch'
}
</script>

<style lang="stylus" scoped>
  @import '~styles/varibles.styl'
  .search
    height: .72rem
    background: $bgColor
    padding: 0 .2rem
    .search-input
      box-sizing: border-box
      padding: 0 .2rem
      width: 100%
      height: .62rem
      line-height : .62rem
      text-align: center
      border-radius: .06rem
      color: #666
</style>
