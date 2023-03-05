<template>
  <div
    ref="CurrentInCompareBarChart"
    style="width: 100%; height: 100%"
  ></div>
</template>
<script>
import * as echarts from 'echarts'
let chart = null
export default {
  props: {
    title: String,
    data: Object
  },
  mounted() {
  },
  methods: {
    initChart () {
      if (null != chart && undefined != chart) {
        chart.dispose()
      }
      chart = this.$echarts.init(this.$refs.CurrentInCompareBarChart)
      this.setOptions()

    },
    setOptions() {
      let option = {
        title: {
          text: this.title,
          x: 'center',
          y: 0,
          textStyle: {
            color: '#B4B4B4',
            fontSize: 14,
            fontWeight: 'normal',
          },

        },
        // backgroundColor: '#191E40',
        tooltip: {
          trigger: 'axis',
          backgroundColor: 'rgba(255,255,255,0.9)',
          axisPointer: {
            type: 'shadow',
            label: {
              show: true,
              backgroundColor: '#7B7DDC'
            }
          }
        },
        legend: {
          data: ['新增确诊'],
          textStyle: {
            color: '#B4B4B4'
          },
          top: '5%',
        },
        grid: {
          x: '12%',
          width: '82%',
          y: '12%',
        },
        xAxis: {
          data: this.data.dateList,
          axisLine: {
            lineStyle: {
              color: '#B4B4B4'
            }
          },
          axisTick: {
            show: false,
          },
        },
        yAxis: [{
          splitLine: { show: false },
          axisLine: {
            lineStyle: {
              color: '#B4B4B4',
            }
          },
          axisLabel: {
            formatter: '{value} ',
          }
        },
        {
          splitLine: { show: false },
          axisLine: {
            lineStyle: {
              color: '#B4B4B4',
            }
          },
          axisLabel: {
            formatter: '{value} ',
          }
        }],
        series: [
          {
            name: '新增确诊病例',
            type: 'bar',
            barWidth: 10,
            itemStyle: {
              normal: {
                barBorderRadius: 5,
                color: new echarts.graphic.LinearGradient(
                  0, 0, 0, 1,
                  [
                    { offset: 0, color: '#956FD4' },
                    { offset: 1, color: '#3EACE5' }
                  ]
                )
              }
            },
            data: this.data.currentConfirmedIncrList
          },
     
        ]
      }
      chart.setOption(option)
    }
  },
  watch: {
    data: {
      handler (newValue, oldValue) {
        if (oldValue != newValue) {
          this.setOptions()
        console.log(this.data,232)

        }
      },
      deep: true
    }
  }
}
</script>