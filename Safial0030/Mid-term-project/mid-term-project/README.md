# mid-term-project

## Project setup

npm install

See [Configuration Reference](https://cli.vuejs.org/config/).

The project involves creating a temperature chart that displays real-time temperature data using Vue.js and Chart.js. Here is a summary of the steps applied for the whole project:

Start by setting up a new Vue.js project and installing the necessary dependencies, including Vue.js and Chart.js.

Create a new component called TemperatureChart.vue. This component will contain the line chart for displaying the temperature data.

In the TemperatureChart.vue component, import the required modules from Chart.js, including the LineController, CategoryScale, LinearScale, PointElement, LineElement, and Title.

Register the imported modules with the Chart.js library using the Chart.register() method.

Set up the reactive data properties for the chart in the TemperatureChart.vue component. This includes the chart data, labels, datasets, and options.

Use the ref function from the Vue Composition API to create a reference to the chart canvas element.

Implement the updateChartData() function, which generates random temperature data and updates the chart's data and labels.

Use the onMounted lifecycle hook to initialize the chart when the component is mounted. Inside the hook, create a new Chart instance and pass in the chart canvas reference, data, and options.

Set up a timer using setInterval() to continuously update the chart data at a specific interval.

Create a separate Navbar.vue component to display the navigation bar. Customize the component based on your project's requirements.

In the main App.vue component, import and register both the Navbar and TemperatureChart components.

Use the imported components in the template section of App.vue. Place the Navbar component at the top and the TemperatureChart component below it. You can also include other components or content as needed.

Style the components using CSS or any other preferred styling approach. Customize the styles based on your project's design requirements.

This summary provides an overview of the steps applied in the project. Please note that the actual implementation may vary based on your specific project structure and requirements. Make sure to adjust the code accordingly and install the necessary dependencies before running the project.
