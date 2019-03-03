<template>
    <div>
      <div class="title">周末去哪儿</div>
      <ul>
        <li class="border-bottom" v-for="item of itemList" :key="item.id">
          <div class="item-image-wrapper">
            <img class="item-image" :src="item.itemUrl"/>
          </div>
          <div class="item-info">
            <p class="item-title" v-text="item.itemTitle"></p>
            <p class="item-desc" v-text="item.itemDesc"></p>
          </div>
        </li>
      </ul>
    </div>
</template>

<script>
export default {
  name: 'HomeWeekend',
  data () {
    return {
      itemList: [
        {
          id: '0001',
          itemUrl: 'http://img1.qunarzz.com/sight/source/1505/7d/df6ff468331c43.jpg_r_640x214_1f3783d0.jpg',
          itemTitle: '大连海洋博物馆',
          itemDesc: '浪漫大连首站',
          itemButtonName: '查看详情'
        },
        {
          id: '0002',
          itemUrl: 'http://img1.qunarzz.com/sight/source/1505/7d/df6ff468331c43.jpg_r_640x214_1f3783d0.jpg',
          itemTitle: '大连海洋博物馆',
          itemDesc: '浪漫大连首站',
          itemButtonName: '查看详情'
        },
        {
          id: '0003',
          itemUrl: 'http://img1.qunarzz.com/sight/source/1505/7d/df6ff468331c43.jpg_r_640x214_1f3783d0.jpg',
          itemTitle: '大连海洋博物馆',
          itemDesc: '浪漫大连首站',
          itemButtonName: '查看详情'
        }
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/mixins.styl'
  .title
    line-height : .8rem
    background: #eee
    text-indent: .2rem
    margin-top: .2rem
    .item-image-wrapper
      overflow : hidden
      height: 0
      padding-bottom : 33.9%
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
