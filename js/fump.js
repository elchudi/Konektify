function loadAudio(div, text, lang_in, lang_out, duration) {
    urlAux = "http://www.waccess-project.com:6770/ade_h"
     jQuery.ajax({
                type:'POST',
                url: urlAux,
                contentType: 'text/plain',
                data: encodeURIComponent(text),
                success: function(msg) { jQuery("#"+div).html("<audio src=\"http://www.waccess-project.com/ADE/"+msg+"\" controls>Your browser does not support the <code>audio</code> element</audio>");},
                dataType: 'text'
        });

}
