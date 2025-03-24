<template>
  <div>
    <Plotly :data="plotData" :layout="layout" />
  </div>
</template>

<script>
import { Plotly } from 'vue-plotly'

export default {
  data() {
    return {
      plotData: [{ x: [1, 2, 3], y: [2, 4, 6], type: 'scatter' }],
      layout: { title: 'Risultati Simulazione' }
    }
  }
}
</script>