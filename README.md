# Graph Parser and Visualizator App

Introducing the Graph Parser and Visualizator App! Built with component-driven development using Django, this app has independent components including the Core, XML parser, JSON parser, D3 Simple Visualizator, and D3 Complex Visualizator. With its powerful parsing and visualization capabilities, you can turn complex data into beautiful and informative visualizations!

With its component-driven architecture, you can plug in additional components like puzzles to further enhance the functionality of the app. So not only can you handle large datasets with ease, but you can also customize the app to suit your specific needs.



https://user-images.githubusercontent.com/51921035/232169376-0ed6f5d0-e48b-4c66-a9ba-d31fd92d5556.mp4



## Components

### Core
The Core component is the backbone of the Graph Parser and Visualizator App, connecting all the other components together seamlessly. It comes equipped with a variety of powerful features, including built-in search and filter capabilities, making it easy to find and manipulate data within the app.

Additionally, the Core component features a tree-view that resembles a file system, allowing for intuitive navigation of the data. A bird's-eye view and a main canvas are also included, providing multiple perspectives on the data and making it easy to spot patterns and trends.

Overall, the Core component is a crucial part of the app's functionality, providing the necessary tools to manage and visualize complex data.

### XML Parser

The XML Parser component of the Graph Parser and Visualizator App is a powerful tool for parsing and visualizing XML data. With its advanced parsing capabilities, it can handle any XML data and represent it as a graph.

One of the key features of the XML Parser is its support for cyclic graphs. This is a particularly important feature for handling complex data structures that may have circular references. With the XML Parser, you can easily convert your XML data into a graph representation, making it easy to identify patterns, trends, and relationships within your data.

### JSON Parser
The JSON Parser component of the Graph Parser and Visualizator App is another powerful tool for parsing and visualizing data. With its advanced parsing capabilities, it can handle any JSON data and represent it as a graph.

Similar to the XML Parser, the JSON Parser also supports cyclic graphs, making it possible to handle complex data structures that may have circular references.

### Simple Visualizer

The D3 Simple Visualizer plugin is a great way to get a high-level overview of your data. Using the d3.js library, it represents each node in the graph as a circle marked with a unique ID number, and edges between nodes are represented by lines connecting the circles.

One of the key features of this plugin is its implementation of a force layout algorithm, which simulates physical forces between nodes to create a visually appealing and intuitive representation of the data. This makes it easy to identify clusters, trends, and patterns within the data.

Overall, the D3 Simple Visualizer plugin is ideal for users who want a quick and easy way to visualize their data without getting bogged down in too many details.

### Complex Visualizer
The D3 ComplexVisualizer plugin is a powerful tool for visualizing data within the Graph Parser and Visualizator App. Using the d3.js library, it represents each node in the graph as a rectangle with a title that includes the name and ID of the node, and content that represents the attributes of the node as key-value pairs.

Edges between nodes are represented by lines connecting the rectangles, and like the D3 Simple Visualizer plugin, the D3 ComplexVisualizer plugin also implements a force layout algorithm to create an intuitive and visually appealing representation of the data.

Unlike the D3 Simple Visualizer plugin, however, the D3 ComplexVisualizer plugin is ideal for users who want to see all the details for each node in the graph. This can be particularly useful when working with complex datasets with many attributes or when trying to identify specific patterns or relationships within the data.

The D3 ComplexVisualizer plugin is not only great for seeing all the details of each node, but it's also a valuable tool for search and filtering. With its rectangular representation of nodes and clear display of key-value pairs, it's easy to search for specific nodes based on their attributes.
## Installation


1. Open project folder and open terminal to create virtual enviroment 
```cmd
  py -m venv env
```

2. Activate virtual enviroment
```cmd
  env/Scripts/Activate
```

3. Run script
```cmd
    python run.py
```
4. Navigate to django project
```cmd
cd GraphVisualizer/django_project
``` 
5. Run server
```cmd
    python manage.py runserver
```

6. Open your browser and visit  http://127.0.0.1:8000/ and have fun!
## Authors

- [Jovan Jokić](https://github.com/jokicjovan)
- [Vlada Dević](https://github.com/ForLoop111)
- [Jovan Šerbedžija](https://github.com/serbedzijajovan)
- [Vukašin Bogdanović](https://github.com/vukasinb7)
