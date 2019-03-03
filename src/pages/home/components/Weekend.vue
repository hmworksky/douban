<template>
    <div>
      <div class="title">周末去哪儿</div>
      <ul>
        <li class="border-bottom" v-for="item of list" :key="item.id">
          <div class="item-image-wrapper">
            <img class="item-image" :src="item.imgUrl"/>
          </div>
          <div class="item-info">
            <p class="item-title" v-text="item.title"></p>
            <p class="item-desc" v-text="item.desc"></p>
          </div>
        </li>
      </ul>
    </div>
</template>

<script>
export default {
  name: 'HomeWeekend',
  props: {
    list: Array
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/mixins.styl'
  .title
    line-height : .8rem
    background: #eee
    text-indent: .2rem
    .item-image-wrapper
      overflow : hidden
      height: 0
      padding-bottom : 33.43%
      .item-image
        width: 100%
    .item-info
      padding: .1rem
      .item-title
        line-height : .54rem
        font-size: .32rem
        ellipsis()
      .item-desc
        line-height: .4rem
        color: #ccc
        ellipsis()
</style>
