---
layout: default
title: Cursos
subtitle: Red de Ciencia de Datos para la Conservación de la Biodiversidad Mesoamericana
permalink: /courses.html
date: 12-12-2023
author: María Mora Cross
full-width: true
---

# Cursos

<table>
  <thead>
    <tr>
      <th>Programa del curso</th>
      <th style="text-align: center;">Inicio</th>
      <th style="text-align: center;">Fin</th>
      <th>Instructores</th>
      <th style="text-align: center;">Proyectos del curso</th>
    </tr>
  </thead>
  <tbody>
    {% for curso in site.data.courses %}
    <tr>
      <td><a href="{{ curso.programa }}">{{ curso.nombre }}</a></td>
      <td>{{ curso.inicio }}</td>
      <td>{{ curso.fin }}</td>
      <td>{{ curso.instructores }}</td>
      {% if curso.proyectos == "En proceso" %}
        <td style="text-align: center;">{{ curso.proyectos }}</td>
      {% else %}
        <td style="text-align: center;">
            <a
              href="{{ curso.proyectos }}"
              class="material-symbols-outlined"
              style="color: #ff5100;"
            >
                folder_open
            </a>
        </td>
      {% endif %}
    </tr>
    {% endfor %}
  </tbody>
</table>