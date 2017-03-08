from fanstatic import Group, Library, Resource

library = Library('angular-xeditable', 'resources')

angular_xeditable_css = Resource(
    library, 'css/xeditable.css',
    minified='css/xeditable.min.css')

angular_xeditable_js = Resource(
    library, 'js/xeditable.js',
    minified='js/xeditable.min.js')

angular_xeditable = Group([angular_xeditable_js, angular_xeditable_css])
