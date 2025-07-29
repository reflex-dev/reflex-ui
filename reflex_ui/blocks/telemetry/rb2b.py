"""RB2B (Reveal Bot to Bot) analytics tracking integration for Reflex applications."""

import reflex as rx

# RB2B tracking script template
RB2B_SCRIPT_TEMPLATE: str = """
!function () {{
    var reb2b = window.reb2b = window.reb2b || [];
    if (reb2b.invoked) return;
    reb2b.invoked = true;
    reb2b.methods = ["identify", "collect"];
    reb2b.factory = function (method) {{
        return function () {{
            var args = Array.prototype.slice.call(arguments);
            args.unshift(method);
            reb2b.push(args);
            return reb2b;
        }};
    }};
    for (var i = 0; i < reb2b.methods.length; i++) {{
        var key = reb2b.methods[i];
        reb2b[key] = reb2b.factory(key);
    }}
    reb2b.load = function (key) {{
        var script = document.createElement("script");
        script.type = "text/javascript";
        script.async = true;
        script.src = "https://s3-us-west-2.amazonaws.com/b2bjsstore/b/" + key + "/reb2b.js.gz";
        var first = document.getElementsByTagName("script")[0];
        first.parentNode.insertBefore(script, first);
    }};
    reb2b.SNIPPET_VERSION = "1.0.1";
    reb2b.load("{api_key}");
}}();
"""


def get_rb2b_trackers(api_key: str) -> rx.Component:
    """Generate RB2B tracking component for a Reflex application.

    Args:
        api_key: Your RB2B API key (found in your RB2B dashboard)

    Returns:
        rx.Component: Script component needed for RB2B tracking
    """
    return rx.script(RB2B_SCRIPT_TEMPLATE.format(api_key=api_key))
