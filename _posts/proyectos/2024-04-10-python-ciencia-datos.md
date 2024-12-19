---
layout: post
author: sjcr23
title: Python para ciencia de datos (Abr 2024)
subtitle: Directorio de los proyectos del curso
categories: [Proyectos de curso]
hidden: [related_posts, navigator]
permalink: "/proyectos/:year-:month-python-ciencia-datos.html"
sidebar: []
---

## Listado de proyectos


<table>
  <thead>
    <tr>
      <th>Nombre del proyecto</th>
      <th>Integrantes</th>
      <th>Ver</th>
    </tr>
  </thead>
  <tbody>
    {% for proyecto in site.data.proyectos.python-ciencia-datos-04-24 %}
    <tr>
      <td>{{ proyecto.nombre }}</td>
      <td>{{ proyecto.integrantes }}</td>
      <td><a href="{{ proyecto.link }}" class="material-symbols-outlined" style="color: #ff5100;">visibility</a></td>
    </tr>
    {% endfor %}
  </tbody>
</table>
