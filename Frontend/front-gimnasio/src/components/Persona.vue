<template>
    <div class="mx-auto max-w-xs">
        <input name="name" type="name"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            placeholder="Nombre Completo">

        <input name="lastName" type="lastName"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
            placeholder="Primer Apellido">

        <input name="lastName" type="lastName"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
            placeholder="Segundo Apellido">

        <select id="countries"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5">
            <option selected>Selecciona Genero</option>
            <option value="">Hombre</option>
            <option value="">Mujer</option>
            <option value="">Otro</option>

        </select>

        <input name="date" type="date"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
            placeholder="">

        <select id="countries"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5">
            <option selected>Selecciona Tipo de Sangre</option>
            <option value="">A+</option>
            <option value="">A-</option>
            <option value="">B+</option>
            <option value="">B-</option>
            <option value="">O+</option>
            <option value="">O-</option>
        </select>

        <lavel for="" class="font-medium">Fotografia</lavel>

        <input name="file" type="file"
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
            placeholder="Fotografia">
        
    </div>

    
    <Tabla></Tabla>
                        <h4 class="pt-8 pb-6 font-bold text-3xl dark:text-gray-400 text-center cursor-default">
                            Datos de acceso
                        </h4>
                        
</template> 

<script>
import Tabla from './Tabla.vue'
export default {
    components: { 
        Tabla
    }
}
</script>