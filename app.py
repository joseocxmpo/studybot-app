<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>StudyBot</title>
<style>
  body{font-family:system-ui,sans-serif;max-width:560px;margin:2rem auto;padding:0 1rem;color:#222}
  h1{margin-bottom:.2rem} p.sub{color:#666;margin-top:0}
  .row{display:flex;justify-content:space-between;align-items:center;padding:.45rem 0;border-bottom:1px solid #eee}
  select{padding:.3rem .5rem;font-size:1rem}
  button{margin-top:1rem;padding:.7rem 1.4rem;font-size:1rem;border:0;border-radius:8px;background:#2b5fd9;color:#fff;cursor:pointer}
  .res{margin-top:1.5rem;padding:1rem;border-radius:10px;text-align:center;font-size:1.4rem;font-weight:700}
  .APTO{background:#e3f6e8;color:#14702f}.NO{background:#fde8e8;color:#a32020}
  .err{margin-top:1rem;padding:.8rem;background:#fff3cd;border-radius:8px}
  small{display:block;font-weight:400;font-size:.85rem;margin-top:.3rem}
</style>
</head>
<body>
<h1>StudyBot</h1>
<p class="sub">¿Es apto este lugar para una sesión de estudio de 30 min en el campus central?</p>
<form method="post">
  {% for c in features %}
  <div class="row">
    <label for="{{ c }}">{{ etiquetas[c] }}</label>
    <select name="{{ c }}" id="{{ c }}" required>
      <option value="0" {% if valores.get(c) == 0 %}selected{% endif %}>No (0)</option>
      <option value="1" {% if valores.get(c) == 1 %}selected{% endif %}>Sí (1)</option>
    </select>
  </div>
  {% endfor %}
  <button type="submit">Predecir</button>
</form>
{% if error %}<div class="err">{{ error }}</div>{% endif %}
{% if resultado %}
<div class="res {{ 'APTO' if resultado == 'APTO' else 'NO' }}">
  {{ resultado }}
  <small>Probabilidad de APTO según el modelo: {{ '%.0f' % (prob*100) }}%</small>
</div>
{% endif %}
</body>
</html>
