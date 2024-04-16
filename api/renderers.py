from rest_framework import renderers


class BlogPostJSONRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Check if the view throws an error
        if isinstance(data, dict) and 'detail' in data:
            return super().render(data)

        # Modify the data as needed
        # For example, adding additional information or changing the structure
        return super().render(data)
