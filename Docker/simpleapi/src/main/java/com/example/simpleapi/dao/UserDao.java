package com.example.simpleapi.dao;

import com.example.simpleapi.dto.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserDao extends JpaRepository<User,Long> {
}
