package com.example.demo;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;

@Configuration 
public class MyWebmvcConfigurerAdapter extends WebMvcConfigurerAdapter{
	
	@Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/back/**").addResourceLocations("classpath:/back/");
        super.addResourceHandlers(registry);
	}
	
}
