# dbt: Modelado y Transformación de Datos

> "dbt permite transformar, documentar y testear datos con SQL de forma colaborativa."

---

## 🧬 ¿Qué es dbt?

dbt (data build tool) es una herramienta open source para modelar, transformar y documentar datos en el data warehouse usando SQL. Facilita la colaboración, el versionado y el testing de modelos de datos.

---

## 🛠️ Componentes Clave

- **Models:** Scripts SQL que definen transformaciones.
- **Seeds:** Datos estáticos para pruebas y referencia.
- **Snapshots:** Versionado histórico de datos.
- **Tests:** Validaciones automáticas de calidad y consistencia.
- **Docs:** Documentación interactiva de modelos y relaciones.

---

## 💡 Buenas Prácticas

!!! tip "Versiona y documenta cada modelo"
    Usa descripciones, docstrings y control de versiones en tus scripts.

!!! info "Automatiza el testing"
    Implementa tests de unicidad, nulos y relaciones para asegurar calidad.

!!! success "Integra con CI/CD"
    Ejecuta dbt en pipelines automáticos para validar y desplegar cambios.

---

## 📝 Ejemplo de Modelo y Test en dbt

```sql
-- models/ventas_diarias.sql
SELECT fecha, SUM(monto) AS total
FROM ventas
GROUP BY fecha;
```

```yaml
# tests/ventas_diarias.yml
tests:
  - unique:
      column_name: fecha
  - not_null:
      column_name: total
```

---

## 📚 Recursos

- [dbt Documentation](https://docs.getdbt.com/docs/introduction)
- [Awesome dbt](https://github.com/tnightengale/awesome-dbt)
- [dbt Cloud](https://www.getdbt.com/product/dbt-cloud/)
- [dbt Best Practices](https://docs.getdbt.com/docs/best-practices)

---

¿Quieres ver ejemplos avanzados o notebooks embebidos? ¡Explora la sección Notebooks!
