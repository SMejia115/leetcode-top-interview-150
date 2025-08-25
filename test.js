async function esperarOk() {
  const url = "https://sistema.extraboletas.com/controlador/fachada.php";

  const body = new URLSearchParams({
    clase: "Ventas",
    oper: "descuentosVW",
    temporada: "1331",
    evento: "3371",
    sector: "4593",
    tipoventas: "1"
  });

  let ok = false;

  while (!ok) {
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        body: body.toString()
      });

      const data = await response.json();
      console.log("Respuesta:", data);

      if (data.ok === true) {
        ok = true;
        console.log("✅ ¡Se recibió ok=true!");
        return data;
      }

      await new Promise(r => setTimeout(r, 1000)); // espera 1s
    } catch (err) {
      console.error("Error en la petición:", err);
      await new Promise(r => setTimeout(r, 2000));
    }
  }
}

esperarOk();
